import os 
import secrets
from Document_Summarizer import logger
from Document_Summarizer.utils.common import allowed_file,create_directories
from Document_Summarizer.pipeline.stage_03_prompt_and_chain import PromptAndChainPipeline
from Document_Summarizer.pipeline.stage_02_data_processing import UploadFileProcessingPipeline

from flask import Flask, request, render_template,redirect,url_for,flash,session,send_file



app = Flask(__name__)


upload_file                                 = UploadFileProcessingPipeline()
upload_file_processing,upload_file_config   = upload_file.main()
UPLOAD_FOLDER                   = 'upload_file'
DOWNLOAD_FOLDER                 = os.path.join(UPLOAD_FOLDER,'download')
app.config["UPLOAD_FOLDER"]     = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH']= 1 * 1024 * 1024  # 1 MB limit
secret_key                      = secrets.token_hex(16) 
app.secret_key                  = os.environ.get(secret_key, 'default_secret_key')


if not os.path.exists(UPLOAD_FOLDER):
    logger.info(f"directory {UPLOAD_FOLDER} is created")
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(DOWNLOAD_FOLDER):
    logger.info(f"directory {DOWNLOAD_FOLDER} is created")
    os.makedirs(DOWNLOAD_FOLDER)


@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    
    if file and allowed_file(file.filename):
        filename        = file.filename
        file_extension  = filename.rsplit('.', 1)[1].lower()

        new_file_path   = None
        if file_extension == "pdf":
            new_file_path = upload_file_config.pdf_file_path
            logger.info(f"Renaming PDF file: {filename} -> {new_file_path}")
            file.save(new_file_path)

        elif file_extension == "txt":
            new_file_path = upload_file_config.text_file_path
            logger.info(f"Renaming TXT file: {filename} -> {new_file_path}")
            file.save(new_file_path)

        elif file_extension in ["doc", "docx", "docs"]:
            new_file_path = upload_file_config.docs_file_path
            logger.info(f"Renaming DOC/DOCX file: {filename} -> {new_file_path}")
            file.save(new_file_path) 
    
        try:
            processed_data = upload_file_processing(file_extension)
            logger.info(f"File {filename} processed successfully")

            prompt_pipeline = PromptAndChainPipeline()
            chain           = prompt_pipeline.main()

            summary_output  = chain.invoke(processed_data)
            logger.info(f"Summary generated successfully for file {filename}")

            # Store the summary and filename in the session
            session['summary'] = summary_output
            session['filename'] = filename

            # Redirect to the summary page
            return redirect('/summary')

        except Exception as e:
            logger.error(f"Error processing file {filename}: {str(e)}")
            flash('An error occurred during file processing. Please try again.')
            return redirect(request.url)

    flash('Invalid file format or no file selected')
    return redirect(request.url)

@app.route('/summary')
def summary():
    # Fetch summary from session
    summary_output  = session.get('summary', None)
    if not summary_output:
        flash('No summary available. Please upload a file first.')
        return redirect('/')

    return render_template('download.html', summary=summary_output)


@app.route('/download-summary')
def download_summary():
    summary_output  = session.get('summary', None)
    filename        = session.get('filename', None)

    if filename and summary_output:
        summary_file_path = os.path.join(DOWNLOAD_FOLDER, 'summary.txt')

        with open(summary_file_path, 'w') as f:
            f.write(summary_output)
        logger.info(f"Summary saved to {summary_file_path}")

        return send_file(summary_file_path, as_attachment=True, download_name='summary.txt')
    else:
        flash('No summary available. Please upload and process a file first.')
        return redirect('/')

    

if __name__ == '__main__':
    app.run(debug=True)



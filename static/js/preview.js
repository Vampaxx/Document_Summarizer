
document.addEventListener('DOMContentLoaded', function () {
    const fileInput     = document.getElementById('file-input');
    const dropZone      = document.getElementById('drop-zone');
    const summarizeBtn  = document.getElementById('Summarize-btn');
    const previewBox    = document.getElementById('preview-box');
    const previewContent= document.getElementById('preview-content');
    const wrapper       = document.querySelector('.wrapper');

    dropZone.addEventListener('dragover', (event) => {
        event.preventDefault();
        dropZone.classList.add('dragging');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('dragging');
    });

    dropZone.addEventListener('drop', (event) => {
        event.preventDefault();
        dropZone.classList.remove('dragging');
        const droppedFiles = event.dataTransfer.files;
        if (droppedFiles.length > 0) {
            fileInput.files = droppedFiles;
            console.log('File dropped:', droppedFiles[0].name);
            showPreview(droppedFiles[0]); // Show preview for the dropped file
        }
    });

    fileInput.addEventListener('change', handleFilePreview);

    summarizeBtn.addEventListener('click', async (event) => {
        event.preventDefault();
        const file = fileInput.files[0];
        if (!file) {
            alert('Please select a file to summarize');
            return;
        }
        const formData = new FormData();
        formData.append('file', file);
        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                window.location.href = '/summary';
            } else {
                alert('Failed to process the file.');
            }
        } catch (error) {
            console.error('Error during file upload:', error);
            alert('An error occurred while uploading the file.');
        }
    });

    function handleFilePreview(event) {
        const file = event.target.files[0];
        showPreview(file); // Show preview for the selected file
    }

    function showPreview(file) {
        if (!file) return;
        previewBox.classList.remove('hidden');
        previewBox.classList.add('show');
        wrapper.classList.remove('centered');
        wrapper.classList.add('shifted'); // Move the container to the left

        previewContent.innerHTML = `<p><strong>File Name:</strong> ${file.name}</p>`;

        // Preview for text files
        if (file.type === 'text/plain') {
            const reader = new FileReader();
            reader.onload = (e) => {
                previewContent.innerHTML += `<p><strong>Content:</strong></p><pre>${e.target.result}</pre>`;
            };
            reader.readAsText(file);

        // Preview for PDF files
        } else if (file.type === 'application/pdf') {
            const reader = new FileReader();
            reader.onload = (e) => {
                const pdfData       = new Uint8Array(e.target.result);
                const loadingTask   = pdfjsLib.getDocument(pdfData);
                loadingTask.promise.then((pdf) => {
                    previewContent.innerHTML += '<p><strong>PDF Preview:</strong></p>';
                    renderPDF(pdf);
                }).catch((error) => {
                    previewContent.innerHTML += '<p>Error loading PDF: ' + error.message + '</p>';
                });
            };
            reader.readAsArrayBuffer(file);

        // Preview for DOCX files
        } else if (file.type === 'application/vnd.openxmlformats-officedocument.wordprocessingml.document') {
            const reader = new FileReader();
            reader.onload = (e) => {
                const arrayBuffer   = e.target.result;
                const zip           = new JSZip();
                zip.loadAsync(arrayBuffer).then((contents) => {
                    return zip.file("word/document.xml").async("string");
                }).then((content) => {
                    const parser    = new DOMParser();
                    const xmlDoc    = parser.parseFromString(content, "text/xml");
                    const text      = xmlDoc.getElementsByTagName("w:t");
                    let docText = "";
                    for (let i = 0; i < text.length; i++) {
                        docText += text[i].textContent + " ";
                    }
                    previewContent.innerHTML += `<p><strong>DOCX Content:</strong></p><pre>${docText}</pre>`;
                }).catch((error) => {
                    previewContent.innerHTML += '<p>Error loading DOCX: ' + error.message + '</p>';
                });
            };
            reader.readAsArrayBuffer(file);

        } else {
            previewContent.innerHTML += '<p>Preview not available for this file type.</p>';
        }
    }

    function renderPDF(pdf) {
        const numPages = pdf.numPages;

        for (let pageNum = 1; pageNum <= numPages; pageNum++) {
            pdf.getPage(pageNum).then((page) => {
                const scale     = 1.5;
                const viewport  = page.getViewport({ scale: scale });
                const canvas    = document.createElement('canvas');
                canvas.classList.add('pdf-preview-canvas');
                previewContent.appendChild(canvas);
                
                const context   = canvas.getContext('2d');
                canvas.height   = viewport.height;
                canvas.width    = viewport.width;

                const renderContext = {
                    canvasContext: context,
                    viewport: viewport,
                };
                page.render(renderContext);
            });
        }
    }
});






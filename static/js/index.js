// JS for home.html
document.addEventListener('DOMContentLoaded', function () {
    const fileInput     = document.getElementById('file-input');
    const dropZone      = document.getElementById('drop-zone');
    const summarizeBtn  = document.getElementById('Summarize-btn');
  
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
      }
    });
  
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
  });
  
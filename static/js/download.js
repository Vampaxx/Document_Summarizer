// JS for summarize.html
document.addEventListener('DOMContentLoaded', function () {
    const downloadBtn = document.querySelector('.download-button');
  
    downloadBtn.addEventListener('click', (event) => {
      event.preventDefault();
      fetch('/download-summary')
        .then((response) => {
          if (response.ok) {
            return response.blob();
          } else {
            throw new Error('Failed to download the summary');
          }
        })
        .then((blob) => {
          const downloadUrl = URL.createObjectURL(blob);
          const a           = document.createElement('a');
          a.href            = downloadUrl;
          a.download        = 'summary.txt';
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);
        })
        .catch((error) => {
          console.error('Error during summary download:', error);
          alert('An error occurred while downloading the summary.');
        });
    });
  });
  
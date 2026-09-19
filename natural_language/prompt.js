(() => {
  const button = document.querySelector('.copy-prompt');
  const prompt = document.querySelector('#starting-prompt code');
  const status = document.querySelector('#copy-status');
  if (!button || !prompt || !status) return;

  button.hidden = false;
  let reset;
  button.addEventListener('click', async () => {
    clearTimeout(reset);
    try {
      await navigator.clipboard.writeText(prompt.textContent.trim());
      button.textContent = 'Copied!';
      status.textContent = 'Prompt copied to clipboard.';
    } catch {
      // Leave the text selected for manual copying if clipboard access is denied.
      const range = document.createRange();
      range.selectNodeContents(prompt);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      button.textContent = 'Select & copy';
      status.textContent = 'Could not copy automatically. The prompt is selected; use your device’s copy command.';
    }
    reset = setTimeout(() => {
      button.textContent = 'Copy';
      status.textContent = '';
    }, 5000);
  });
})();

(() => {
  let theme;
  try { theme = localStorage.getItem('white-paper-theme'); } catch { /* Storage may be disabled. */ }
  document.documentElement.dataset.theme = theme === 'dark' || theme === 'light'
    ? theme : (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
})();

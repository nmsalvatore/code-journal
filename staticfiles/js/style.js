// remove all labels from forms
labels = document.querySelectorAll('form p label')
labels.forEach(label => {
    label.style.display = 'none';
});

// autogrow textarea
const growers = document.querySelectorAll('.grow-wrap');
growers.forEach((grower) => {
  const textarea = grower.querySelector('textarea');
  textarea.addEventListener('input', () => {
    grower.dataset.replicatedValue = textarea.value;
  });
});
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

// add comma to any item separated by a space for array conversion
const tags = document.getElementById('id_tags');
tags.addEventListener('keydown', e => {
  const lastChar = tags.value.slice(-1)
  if (e.code == 'Space' && lastChar != ',' && lastChar != ' ') {
    tags.value += ',';
  }
})
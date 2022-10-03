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
  document.addEventListener('DOMContentLoaded', () => {
    grower.dataset.replicatedValue = textarea.value;
  })
});

// add comma to any item separated by a space for array conversion
const tags = document.getElementById('id_tags');
if (tags) {
  tags.addEventListener('keydown', e => {
    const lastChar = tags.value.slice(-1)
    if (e.code == 'Space' && lastChar != ',' && lastChar != ' ') {
      tags.value += ',';
    }
  });  
}

// remove all p elements with empty value
const pElements = document.querySelectorAll('p');
document.addEventListener('DOMContentLoaded', () => {
    for (let p of pElements) {
      if (p.textContent == '') {
        p.style.display = 'none';
      }
    }
});

// toggle tag menu
const menuIcon = document.querySelector('.menu.icon');
if (menuIcon) {
  menuIcon.addEventListener('click', () => {
    const tagDirectory = document.querySelector('ul.tag-directory');
    if (!tagDirectory.style.display || tagDirectory.style.display == 'none') {
      tagDirectory.style.display = 'block';
    } else {
      tagDirectory.style.display = 'none'
    }
  });
}

// set current-tag to 'all' if tag value is empty
const currentTag = document.querySelector('.current-tag')
if (currentTag) {
  if (currentTag.textContent == '#') {
    currentTag.textContent += 'all'
  }
}

// word counter
const postBody = document.getElementById('id_body');
if (postBody) {
  postBody.addEventListener('keyup', () => {
      words = postBody.value.split(' ');
      wordCount = words.length;
      wordCounter = document.getElementById('word_counter');
      
      if (words.includes('')) {
        wordCount--;
      } 

      wordCounter.textContent = 'Word Count: ' + wordCount;
  });

  document.addEventListener('DOMContentLoaded', () => {
    words = postBody.value.split(' ');
    wordCount = words.length;
    wordCounter = document.getElementById('word_counter');
    
    if (words.includes('')) {
      wordCount--;
    } 

    wordCounter.textContent = 'Word Count: ' + wordCount;
});
}
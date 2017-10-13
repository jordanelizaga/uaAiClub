let message = document.querySelectorAll('.message');

for (var i = 0; i < message.length; i++) {
  message[i].addEventListener('mouseover' , function() {
    removeHidden(this);
  });
  message[i].addEventListener('mouseleave', function() {
    addHidden(this);
  });
}

function addHidden(el) {
  classList = el.nextElementSibling.classList;
  if (!classList.contains('hidden'))
    classList.add('hidden');
};

function removeHidden(el) {
  classList = el.nextElementSibling.classList;
  if (classList.contains('hidden'))
    classList.remove('hidden');
};

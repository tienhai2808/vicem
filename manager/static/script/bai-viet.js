const formPost = document.querySelector('.form-post')
formPost.querySelectorAll('input').forEach((input) => {
  input.classList.add('form-control')
})
formPost.querySelector('select').classList.add('form-select')
formPost.querySelector('textarea').classList.add('form-control')
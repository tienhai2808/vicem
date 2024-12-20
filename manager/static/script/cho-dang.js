const divForm = document.querySelector('.form-time')
const btnClose = divForm.querySelector('.fa-xmark')
btnClose.addEventListener('click', () => {
  if (!divForm.classList.contains('d-none')) {
    divForm.classList.add('d-none')
  }
})

const btnPosts = document.querySelectorAll('.btn-post')
const formSubmit = divForm.querySelector('form')
const btnDeletes = document.querySelectorAll('.btn-delete')
if (btnPosts.length > 0) {
  btnPosts.forEach((btn) => {
    btn.addEventListener('click' ,() => {
      if (divForm.classList.contains('d-none')) {
        divForm.classList.remove('d-none')
      }
      const btnSubmit = formSubmit.querySelector('button')
      const inputStartTime = formSubmit.querySelector('#start_time')
      const inputEndTime = formSubmit.querySelector('#end_time')
      btnSubmit.addEventListener('click', () => {
        if (inputStartTime.value === '' && inputEndTime.value === '') {
          const confirmPost = confirm("Đăng bài viết ở tất cả khung giờ?")
          if (confirmPost) {
            formSubmit.querySelector('#id_post').value = btn.getAttribute('value')
            formSubmit.querySelector('#action').value = 'post' 
            formSubmit.submit()
          }
        } else if (inputStartTime.value === '' || inputEndTime.value === '') {
          alert('Vui lòng chọn khung giờ đăng bài')
          return
        } else {
          const confirmPost = confirm('Đăng bài viết ở khung giờ đã chọn?')
          if (confirmPost) {
            formSubmit.querySelector('#id_post').value = btn.getAttribute('value')
            formSubmit.querySelector('#action').value = 'post' 
            formSubmit.submit()
          }
        }
      })
    })
  })
}

if (btnDeletes.length > 0) {
  btnDeletes.forEach((btn) => {
    btn.addEventListener('click', () => {
      const confirmDelete = confirm('Xác nhận xóa bài viết này?')
      if (confirmDelete) {
        formSubmit.querySelector('#id_post').value = btn.getAttribute('value')
        formSubmit.querySelector('#action').value = 'delete' 
        formSubmit.submit()
      }
    })
  })
}

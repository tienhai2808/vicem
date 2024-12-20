const btnRemoves = document.querySelectorAll('.btn-remove')
const btnDeletes = document.querySelectorAll('.btn-delete')
const formAction = document.querySelector('.form-action')
if (btnRemoves.length > 0) {
  btnRemoves.forEach((btn) => {
    btn.addEventListener('click', () => {
      const confirmRemove = confirm('Xác nhận gỡ bài viết?')
      if (confirmRemove) {
        formAction.querySelector("input[name='id_post']").value = btn.getAttribute('value')
        formAction.querySelector("input[name='action']").value = 'remove'
        formAction.submit()
      }
    })
  })
}

if (btnDeletes.length > 0) {
  btnDeletes.forEach((btn) => {
    btn.addEventListener('click', () => {
      const confirmDelete = confirm('Xác nhận xóa bài viết?')
      if (confirmDelete) {
        formAction.querySelector("input[name='id_post']").value = btn.getAttribute('value')
        formAction.querySelector("input[name='action']").value = 'delete'
        formAction.submit()
      }
    })
  })
}
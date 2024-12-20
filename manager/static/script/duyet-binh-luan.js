const btnConfirms = document.querySelectorAll('.btn-confirm')
const btnDeletes = document.querySelectorAll('.btn-delete')
const formAction = document.querySelector('.form-action')
if (btnConfirms.length > 0) {
  btnConfirms.forEach((btn) => {
    btn.addEventListener('click', () => {
      const confirmCmt = confirm('Duyệt bình luận này?')
      if (confirmCmt) {
        formAction.querySelector("input[name='id_cmt']").value = btn.getAttribute('value')
        formAction.querySelector("input[name='action']").value = 'confirm'
        formAction.submit()
      }
    })
  })
}

if (btnDeletes.length > 0) {
  btnDeletes.forEach((btn) => {
    btn.addEventListener('click', () => {
      const confirmDelete = confirm('Xóa bình luận này?')
      if (confirmDelete) {
        formAction.querySelector("input[name='id_cmt']").value = btn.getAttribute('value')
        formAction.querySelector("input[name='action']").value = 'delete'
        formAction.submit()
      }
    })
  })
}
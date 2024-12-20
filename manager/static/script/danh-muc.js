const btnCreate = document.querySelector('.btn-create')
const divForm = document.querySelector('.form-create')
const btnClose = divForm.querySelector('.fa-xmark')

btnCreate.addEventListener('click', () => {
  divForm.classList.toggle('d-none')
})

btnClose.addEventListener('click', () => {
  if (!divForm.classList.contains('d-none')) {
    divForm.classList.add('d-none')
  }
})


const formDelete = document.querySelector('.form-delete')
const btnDeletes = document.querySelectorAll('.badge')
btnDeletes.forEach((btn) => {
  btn.addEventListener('click', () => {
    const confirmDelete = confirm('Xác nhận xóa danh mục?')
    if (confirmDelete) {
      formDelete.querySelector('[hidden]').value = btn.getAttribute('id')
      formDelete.submit()
    }
  })
})
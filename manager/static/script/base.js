const divAlerts = document.querySelectorAll('.alert-warning')
if (divAlerts.length > 0) {
  divAlerts.forEach((div) => {
    div.querySelector('.close-alert').addEventListener('click', () => {
      div.remove()
    })
  })
}
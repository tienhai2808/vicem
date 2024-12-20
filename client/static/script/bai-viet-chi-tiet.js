const btnShare = document.querySelector('.btn-share')
btnShare.addEventListener('click', async () => {
  if (navigator.share) {
    try {
      await navigator.share({
        title: document.title,
        text: 'Xem bài viết này',
        url: window.location.href
      }) 
    } catch (error) {
      console.log(error)
    }
  } else {
    alert('Trình duyệt không hỗ trợ chia sẻ')
  }
})

const formLike = document.querySelector('.form-like')
const btnLike = document.querySelector('.btn-like')
btnLike.addEventListener('click', () => {
  formLike.submit()
})
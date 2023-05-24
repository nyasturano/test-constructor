document.addEventListener('DOMContentLoaded', () => {
  const theory = document.querySelectorAll('input#theory'),
        practice = document.querySelectorAll('input#practice'),
        all = document.querySelector('#all'),
        vCount = document.querySelector('input#numTasks')
        btn = document.querySelector('button')
        msg = document.querySelector('.block#message')

  
  all.addEventListener('click', () => {
    theory.forEach(check => {
      check.checked = all.checked
    })
    practice.forEach(check => {
      check.checked = all.checked
    })
  })

  theory.forEach(check => {
    check.addEventListener('click', () => all.checked = false)
  })
  practice.forEach(check => {
    check.addEventListener('click', () => all.checked = false)
  })
  
  btn.addEventListener('click', async () => {
    let th_mask = []
    let pr_mask = []
    theory.forEach(check => th_mask.push(check.checked))
    practice.forEach(check => pr_mask.push(check.checked))
    await eel.make_variants(vCount.value, th_mask, pr_mask)
    msg.classList.toggle('active')
    msg.classList.toggle('disabled')
    setTimeout(() => {
      msg.classList.toggle('active')
      msg.classList.toggle('disabled')
    }, 1000)
    // let div = document.createElement('div')
    // div.innerHTML = '<div class="block" style="color: rgb(95, 149, 72);">Варианты успешно сформированы!</div>'
    // document.body.appendChild(div)
  })
  
})
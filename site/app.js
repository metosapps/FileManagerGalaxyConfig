const menuButton=document.querySelector('[data-menu]');
const navigation=document.querySelector('#navigation');
menuButton?.addEventListener('click',()=>{const open=menuButton.getAttribute('aria-expanded')!=='true';menuButton.setAttribute('aria-expanded',String(open));navigation.classList.toggle('is-open',open);menuButton.setAttribute('aria-label',open?'Close navigation':'Open navigation');});
navigation?.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{navigation.classList.remove('is-open');menuButton?.setAttribute('aria-expanded','false');menuButton?.setAttribute('aria-label','Open navigation');}));
const shots=[...document.querySelectorAll('[data-shot]')],dialog=document.querySelector('#gallery-dialog');let selected=0;
function showShot(index){selected=(index+shots.length)%shots.length;const shot=shots[selected];const image=dialog.querySelector('img');image.src=shot.dataset.shot;image.alt=shot.dataset.title;dialog.querySelector('[data-caption]').textContent=`${selected+1} / ${shots.length} · ${shot.dataset.title}`;}
shots.forEach((shot,index)=>shot.addEventListener('click',()=>{if(!dialog?.showModal){window.open(shot.dataset.shot,'_blank','noopener');return;}showShot(index);dialog.showModal();}));
dialog?.querySelector('[data-close]')?.addEventListener('click',()=>dialog.close());
dialog?.querySelector('[data-prev]')?.addEventListener('click',()=>showShot(selected-1));
dialog?.querySelector('[data-next]')?.addEventListener('click',()=>showShot(selected+1));
dialog?.addEventListener('click',event=>{if(event.target===dialog)dialog.close();});
dialog?.addEventListener('keydown',event=>{if(event.key==='ArrowRight'){event.preventDefault();showShot(selected+1);}if(event.key==='ArrowLeft'){event.preventDefault();showShot(selected-1);}});
document.querySelector('[data-copy-email]')?.addEventListener('click',async()=>{const status=document.querySelector('[data-copy-status]');try{await navigator.clipboard.writeText('chennoufo11@gmail.com');status.textContent='Support email copied.';}catch{status.textContent='Email: chennoufo11@gmail.com';}});

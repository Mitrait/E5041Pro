// 3D tilt for blocks and buttons on mouse move (liquid feel)
document.querySelectorAll('.glass, .btn').forEach(el => {
    el.addEventListener('mousemove', e => {
        const rect = el.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        el.style.transform = `translateY(-2px) rotateY(${(x - rect.width / 2) / 10}deg) rotateX(${(y - rect.height / 2) / 10 * -1}deg)`;
    });
    el.addEventListener('mouseleave', () => { el.style.transform = 'translateY(0) rotateY(0) rotateX(0)'; });
});

console.log('Комбинация Metal + Liquid 3D готова');
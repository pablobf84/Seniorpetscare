(function(){
  // Calculadora de edad
  const form = document.querySelector('[data-age-calculator]');
  if(form){
    form.addEventListener('submit', function(e){
      e.preventDefault();
      const years = parseFloat(form.querySelector('#dog-years').value || 0);
      const weight = parseFloat(form.querySelector('#dog-weight').value || 0);
      if(!years || !weight) return;
      const seniorAge = years * (weight > 25 ? 7 : 6);
      const segment = weight > 25 ? 'razas grandes' : 'razas pequeñas';
      const result = `Edad equivalente: ${seniorAge.toFixed(1)} años caninos senior · Recomendado: rampas ortopédicas y suplementos para ${segment}.`;
      const box = document.querySelector('[data-age-result]');
      if(box) box.textContent = result;
    });
  }

  // Filtros
  document.querySelectorAll('[data-filter-input]').forEach((checkbox)=>{
    checkbox.addEventListener('change',()=>{window.location.assign(checkbox.dataset.url);});
  });
  document.querySelectorAll('[data-price-submit]').forEach((btn)=>{
    btn.addEventListener('click',()=>{
      const parent = btn.closest('.filter__range');
      const min = parent.querySelector('#price-min').value;
      const max = parent.querySelector('#price-max').value;
      const url = new URL(window.location.href);
      if(min) url.searchParams.set('filter.v.price.gte', min);
      if(max) url.searchParams.set('filter.v.price.lte', max);
      window.location.assign(url.toString());
    });
  });
  document.querySelectorAll('[data-custom-tag]').forEach((checkbox)=>{
    checkbox.addEventListener('change',()=>{
      const active = Array.from(document.querySelectorAll('[data-custom-tag]:checked')).map(el=>el.dataset.customTag);
      const base = window.location.pathname.replace(/\/$/,'');
      const path = active.length ? `${base}/${active.join('+')}` : base;
      window.location.assign(path + window.location.search);
    });
  });

  // Testimonios
  const carousel = document.querySelector('[data-testimonials-carousel]');
  if(carousel){
    const scroll = (dir)=>{carousel.scrollBy({left: dir * 320, behavior:'smooth'});};
    document.querySelector('[data-prev]')?.addEventListener('click',()=>scroll(-1));
    document.querySelector('[data-next]')?.addEventListener('click',()=>scroll(1));
  }

  // Sticky bar
  const stickyBar = document.querySelector('[data-sticky-bar]');
  if(stickyBar){
    const submitBtn = stickyBar.querySelector('[data-sticky-submit]');
    submitBtn?.addEventListener('click', ()=>{
      document.querySelector('.product-form [type="submit"]')?.click();
    });
  }
})();

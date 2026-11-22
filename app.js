/* ============================================================
   Alquimia Beer — configuração da demonstração
   Altere só estes valores para adaptar a loja.
   ============================================================ */
const WHATSAPP_NUMBER = "5551981630209";
const TAXA_ENTREGA = 6;
const STORAGE_KEY = "alquimia-beer-cart";

/* Horário de funcionamento (minutos a partir de 00:00, fuso America/Sao_Paulo).
   0 = domingo … 6 = sábado. Fecha em 24*60 = meia-noite. */
const HORARIOS = {
  0: { abre: 10 * 60, fecha: 20 * 60, label: "Domingo 10h–20h" },
  1: { abre: 10 * 60, fecha: 22 * 60, label: "Segunda 10h–22h" },
  2: { abre: 10 * 60, fecha: 22 * 60, label: "Terça 10h–22h" },
  3: { abre: 10 * 60, fecha: 22 * 60, label: "Quarta 10h–22h" },
  4: { abre: 10 * 60, fecha: 22 * 60, label: "Quinta 10h–22h" },
  5: { abre: 10 * 60, fecha: 24 * 60, label: "Sexta 10h–00h" },
  6: { abre: 10 * 60, fecha: 24 * 60, label: "Sábado 10h–00h" },
};

const HORARIO_RESUMO = "Seg a Qui 10h–22h · Sex e Sáb 10h–00h · Domingo 10h–20h";

const CATEGORIAS = [
  "Cervejas",
  "Destilados",
  "Vinhos",
  "Energéticos",
  "Refrigerantes e Água",
  "Gelo e Carvão",
  "Combos",
];

const PRODUTOS = [
  { id: "heineken", nome: "Heineken Long Neck", volume: "330ml", preco: 7.9, categoria: "Cervejas", imagem: "img/heineken.svg" },
  { id: "brahma", nome: "Brahma Duplo Malte", volume: "Lata 350ml", preco: 4.49, categoria: "Cervejas", imagem: "img/brahma.svg" },
  { id: "skol", nome: "Skol Pilsen", volume: "Lata 350ml", preco: 3.99, categoria: "Cervejas", imagem: "img/skol.svg" },
  { id: "corona", nome: "Corona Extra", volume: "330ml", preco: 8.9, categoria: "Cervejas", imagem: "img/corona.svg" },
  { id: "original", nome: "Original", volume: "Garrafa 600ml", preco: 9.9, categoria: "Cervejas", imagem: "img/original.svg" },
  { id: "stella", nome: "Stella Artois Long Neck", volume: "330ml", preco: 7.5, categoria: "Cervejas", imagem: "img/stella.svg" },
  { id: "spaten", nome: "Spaten Puro Malte", volume: "Lata 350ml", preco: 5.9, categoria: "Cervejas", imagem: "img/spaten.svg" },
  { id: "smirnoff", nome: "Smirnoff Vodka", volume: "998ml", preco: 49.9, categoria: "Destilados", imagem: "img/smirnoff.svg" },
  { id: "jack", nome: "Jack Daniel's Old No. 7", volume: "1L", preco: 159.9, categoria: "Destilados", imagem: "img/jack.svg" },
  { id: "cachaca51", nome: "Cachaça 51", volume: "965ml", preco: 18.9, categoria: "Destilados", imagem: "img/cachaca51.svg" },
  { id: "tanqueray", nome: "Tanqueray London Dry Gin", volume: "750ml", preco: 129.9, categoria: "Destilados", imagem: "img/tanqueray.svg" },
  { id: "casillero", nome: "Casillero del Diablo Cabernet", volume: "750ml", preco: 59.9, categoria: "Vinhos", imagem: "img/casillero.svg" },
  { id: "miolo", nome: "Miolo Seleção Tinto Seco", volume: "750ml", preco: 39.9, categoria: "Vinhos", imagem: "img/miolo.svg" },
  { id: "salton", nome: "Salton Classic Chardonnay", volume: "750ml", preco: 34.9, categoria: "Vinhos", imagem: "img/salton.svg" },
  { id: "redbull", nome: "Red Bull Energy Drink", volume: "250ml", preco: 9.9, categoria: "Energéticos", imagem: "img/redbull.svg" },
  { id: "monster", nome: "Monster Energy", volume: "473ml", preco: 10.9, categoria: "Energéticos", imagem: "img/monster.svg" },
  { id: "tnt", nome: "TNT Energy Drink", volume: "473ml", preco: 6.9, categoria: "Energéticos", imagem: "img/tnt.svg" },
  { id: "coca", nome: "Coca-Cola", volume: "2L", preco: 9.9, categoria: "Refrigerantes e Água", imagem: "img/coca.svg" },
  { id: "guarana", nome: "Guaraná Antarctica", volume: "2L", preco: 8.5, categoria: "Refrigerantes e Água", imagem: "img/guarana.svg" },
  { id: "crystal", nome: "Água Crystal sem gás", volume: "1,5L", preco: 3.5, categoria: "Refrigerantes e Água", imagem: "img/crystal.svg" },
  { id: "gelo", nome: "Gelo em cubos", volume: "5kg", preco: 12, categoria: "Gelo e Carvão", imagem: "img/gelo.svg" },
  { id: "carvao", nome: "Carvão vegetal", volume: "4kg", preco: 18.9, categoria: "Gelo e Carvão", imagem: "img/carvao.svg" },
  { id: "combo-churras", nome: "Combo Churras", volume: "12 latas + gelo + carvão", preco: 69.9, categoria: "Combos", imagem: "img/combo-churras.svg" },
  { id: "kit-heineken", nome: "Kit Heineken", volume: "6 long necks 330ml", preco: 39.9, categoria: "Combos", imagem: "img/kit-heineken.svg" },
];

/* ----------------- estado ----------------- */
let cart = loadCart();
let categoriaAtiva = "Todas";
let busca = "";

function loadCart() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    const parsed = raw ? JSON.parse(raw) : {};
    return parsed && typeof parsed === "object" ? parsed : {};
  } catch {
    return {};
  }
}

function saveCart() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(cart));
}

function brl(n) {
  return n.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
}

function normalize(s) {
  return String(s)
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "");
}

function qtyOf(id) {
  return cart[id] || 0;
}

function setQty(id, qty) {
  if (qty <= 0) delete cart[id];
  else cart[id] = qty;
  saveCart();
  render();
}

function cartEntries() {
  return Object.entries(cart)
    .map(([id, qty]) => {
      const p = PRODUTOS.find((x) => x.id === id);
      return p ? { ...p, qty } : null;
    })
    .filter(Boolean);
}

function subtotal() {
  return cartEntries().reduce((s, i) => s + i.preco * i.qty, 0);
}

function totalItens() {
  return cartEntries().reduce((s, i) => s + i.qty, 0);
}

/* ----------------- horário ----------------- */
function agoraEmSaoPaulo() {
  const parts = new Intl.DateTimeFormat("en-GB", {
    timeZone: "America/Sao_Paulo",
    weekday: "short",
    hour: "2-digit",
    minute: "2-digit",
    hour12: false,
  }).formatToParts(new Date());
  const get = (t) => parts.find((p) => p.type === t)?.value;
  const map = { sun: 0, mon: 1, tue: 2, wed: 3, thu: 4, fri: 5, sat: 6 };
  const weekday = map[get("weekday").toLowerCase()] ?? new Date().getDay();
  const hour = Number(get("hour"));
  const minute = Number(get("minute"));
  return { weekday, minutes: hour * 60 + minute, hour, minute };
}

function statusHorario() {
  const { weekday, minutes } = agoraEmSaoPaulo();
  const hoje = HORARIOS[weekday];
  const aberto = minutes >= hoje.abre && minutes < hoje.fecha;
  if (aberto) {
    const fechaH = Math.floor(hoje.fecha / 60) % 24;
    const fechaM = hoje.fecha % 60;
    const fecha = `${String(fechaH).padStart(2, "0")}h${fechaM ? String(fechaM).padStart(2, "0") : ""}`;
    return { aberto: true, texto: `Aberto agora · fecha às ${fecha.replace(/h$/, "h")}`, curto: "Aberto agora" };
  }
  if (minutes < hoje.abre) {
    const h = Math.floor(hoje.abre / 60);
    return { aberto: false, texto: `Fechado · abre hoje às ${h}h`, curto: "Fechado agora" };
  }
  const amanha = HORARIOS[(weekday + 1) % 7];
  const h = Math.floor(amanha.abre / 60);
  const dia = weekday === 6 ? "segunda" : "amanhã";
  return { aberto: false, texto: `Fechado · abre ${dia} às ${h}h`, curto: "Fechado agora" };
}

function renderHorario() {
  const s = statusHorario();
  const badge = document.getElementById("horario-badge");
  badge.classList.toggle("is-closed", !s.aberto);
  badge.querySelector(".hours-text").textContent = s.texto;
  document.getElementById("hero-horario").textContent = `${s.texto}. ${HORARIO_RESUMO}. Taxa de entrega para Esteio: ${brl(TAXA_ENTREGA)}.`;
  document.getElementById("footer-hours").textContent = HORARIO_RESUMO;
}

/* ----------------- UI catálogo ----------------- */
function produtosFiltrados() {
  const q = normalize(busca.trim());
  return PRODUTOS.filter((p) => {
    const catOk = categoriaAtiva === "Todas" || p.categoria === categoriaAtiva;
    if (!catOk) return false;
    if (!q) return true;
    return normalize(`${p.nome} ${p.volume} ${p.categoria}`).includes(q);
  });
}

function renderCats() {
  const wrap = document.getElementById("cats-inner");
  const all = ["Todas", ...CATEGORIAS];
  wrap.innerHTML = all
    .map(
      (c) =>
        `<button type="button" class="cat-btn${c === categoriaAtiva ? " is-active" : ""}" data-cat="${escapeHtml(c)}">${escapeHtml(c)}</button>`
    )
    .join("");
}

function renderGrid() {
  const list = produtosFiltrados();
  const grid = document.getElementById("grid");
  const empty = document.getElementById("empty");
  document.getElementById("catalog-count").textContent = `${list.length} ${list.length === 1 ? "item" : "itens"}`;
  empty.hidden = list.length > 0;
  grid.innerHTML = list
    .map((p) => {
      const q = qtyOf(p.id);
      const action =
        q > 0
          ? `<div class="stepper" role="group" aria-label="Quantidade">
              <button type="button" data-act="dec" data-id="${p.id}" aria-label="Diminuir">−</button>
              <span>${q}</span>
              <button type="button" data-act="inc" data-id="${p.id}" aria-label="Aumentar">+</button>
            </div>`
          : `<button type="button" class="btn-add" data-act="inc" data-id="${p.id}">Adicionar</button>`;
      return `<article class="card">
        <div class="card-img"><img src="${p.imagem}" alt="${escapeHtml(p.nome)}" /></div>
        <div class="card-body">
          <h3 class="card-name">${escapeHtml(p.nome)}</h3>
          <p class="card-meta">${escapeHtml(p.volume)}</p>
          <div class="card-foot">
            <span class="price">${brl(p.preco)}</span>
            ${action}
          </div>
        </div>
      </article>`;
    })
    .join("");
}

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

/* ----------------- sacola / checkout ----------------- */
function renderCartChrome() {
  const n = totalItens();
  const count = document.getElementById("cart-count");
  if (n > 0) {
    count.hidden = false;
    count.textContent = String(n);
  } else {
    count.hidden = true;
  }

  const bar = document.getElementById("cart-bar");
  if (n > 0) {
    bar.hidden = false;
    document.body.classList.add("has-cart-bar");
    document.getElementById("cart-bar-info").textContent = `${n} ${n === 1 ? "item" : "itens"} · ${brl(subtotal())}`;
  } else {
    bar.hidden = true;
    document.body.classList.remove("has-cart-bar");
  }
}

function renderDrawer() {
  const body = document.getElementById("drawer-body");
  const form = document.getElementById("checkout");
  const items = cartEntries();
  if (!items.length) {
    body.innerHTML = `<div class="cart-empty">Sua sacola está vazia.<br/>Adicione produtos do cardápio.</div>`;
    form.hidden = true;
    return;
  }
  form.hidden = false;
  body.innerHTML = items
    .map(
      (i) => `<div class="cart-item">
        <img src="${i.imagem}" alt="" />
        <div>
          <h3>${escapeHtml(i.nome)}</h3>
          <p class="meta">${escapeHtml(i.volume)} · ${brl(i.preco)}</p>
          <span class="line">${brl(i.preco * i.qty)}</span>
          <button type="button" class="remove" data-act="del" data-id="${i.id}">Remover</button>
        </div>
        <div class="stepper" role="group" aria-label="Quantidade">
          <button type="button" data-act="dec" data-id="${i.id}" aria-label="Diminuir">−</button>
          <span>${i.qty}</span>
          <button type="button" data-act="inc" data-id="${i.id}" aria-label="Aumentar">+</button>
        </div>
      </div>`
    )
    .join("");

  const sub = subtotal();
  const total = sub + TAXA_ENTREGA;
  document.getElementById("totals").innerHTML = `
    <div><span>Subtotal</span><span>${brl(sub)}</span></div>
    <div><span>Taxa de entrega</span><span>${brl(TAXA_ENTREGA)}</span></div>
    <div class="grand"><span>Total</span><span>${brl(total)}</span></div>
    <p class="tax-note">Taxa de entrega para Esteio e região. Outros bairros podem ser confirmados no WhatsApp.</p>
  `;
}

function openDrawer() {
  const drawer = document.getElementById("drawer");
  const backdrop = document.getElementById("backdrop");
  drawer.hidden = false;
  backdrop.hidden = false;
  requestAnimationFrame(() => drawer.classList.add("is-open"));
  document.body.classList.add("has-drawer");
  document.getElementById("fechar-sacola").focus();
}

function closeDrawer() {
  const drawer = document.getElementById("drawer");
  const backdrop = document.getElementById("backdrop");
  drawer.classList.remove("is-open");
  document.body.classList.remove("has-drawer");
  setTimeout(() => {
    if (!drawer.classList.contains("is-open")) {
      drawer.hidden = true;
      backdrop.hidden = true;
    }
  }, 280);
}

function toast(msg) {
  const el = document.getElementById("toast");
  el.textContent = msg;
  el.hidden = false;
  clearTimeout(toast._t);
  toast._t = setTimeout(() => {
    el.hidden = true;
  }, 1800);
}

/* ----------------- WhatsApp ----------------- */
function montarMensagem(dados) {
  const itens = cartEntries()
    .map((i) => `• ${i.qty}x ${i.nome} (${i.volume}) — ${brl(i.preco * i.qty)}`)
    .join("\n");
  const sub = subtotal();
  const total = sub + TAXA_ENTREGA;
  const linhas = [
    "🍺 *Novo pedido — Alquimia Beer*",
    "",
    "*Itens:*",
    itens,
    "",
    `*Subtotal:* ${brl(sub)}`,
    `*Taxa de entrega:* ${brl(TAXA_ENTREGA)}`,
    `*Total:* ${brl(total)}`,
    "",
    `*Cliente:* ${dados.nome}`,
    `*Endereço:* ${dados.endereco}`,
    `*Bairro:* ${dados.bairro}`,
    `*Pagamento:* ${dados.pagamento}`,
  ];
  if (dados.pagamento === "Dinheiro" && dados.troco) {
    linhas.push(`*Troco para:* ${dados.troco}`);
  }
  if (dados.observacao) {
    linhas.push(`*Obs:* ${dados.observacao}`);
  }
  linhas.push("", "_Pedido enviado pelo site (demonstração)_");
  return linhas.join("\n");
}

function linkWhatsApp(texto) {
  return `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(texto)}`;
}

function greetingLink() {
  return linkWhatsApp("Olá, vim pelo site da Alquimia Beer!");
}

/* ----------------- eventos ----------------- */
function render() {
  renderCats();
  renderGrid();
  renderCartChrome();
  renderDrawer();
}

function onAct(id, act) {
  const atual = qtyOf(id);
  if (act === "inc") {
    setQty(id, atual + 1);
    if (atual === 0) toast("Adicionado à sacola");
  } else if (act === "dec") {
    setQty(id, atual - 1);
  } else if (act === "del") {
    setQty(id, 0);
  }
}

document.addEventListener("click", (e) => {
  const cat = e.target.closest(".cat-btn");
  if (cat) {
    categoriaAtiva = cat.dataset.cat;
    render();
    return;
  }
  const actBtn = e.target.closest("[data-act]");
  if (actBtn) {
    onAct(actBtn.dataset.id, actBtn.dataset.act);
  }
});

document.getElementById("busca").addEventListener("input", (e) => {
  busca = e.target.value;
  renderGrid();
});

document.getElementById("abrir-sacola").addEventListener("click", openDrawer);
document.getElementById("cart-bar").addEventListener("click", openDrawer);
document.getElementById("fechar-sacola").addEventListener("click", closeDrawer);
document.getElementById("backdrop").addEventListener("click", closeDrawer);
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeDrawer();
});

const form = document.getElementById("checkout");
const trocoWrap = document.getElementById("troco-wrap");

function syncTroco() {
  const pag = form.pagamento.value;
  trocoWrap.hidden = pag !== "Dinheiro";
}
form.addEventListener("change", syncTroco);

form.addEventListener("submit", (e) => {
  e.preventDefault();
  if (!cartEntries().length) return;

  const campos = ["nome", "endereco", "bairro"];
  let ok = true;
  for (const name of campos) {
    const el = form[name];
    const vazio = !el.value.trim();
    el.classList.toggle("is-invalid", vazio);
    if (vazio) ok = false;
  }
  const pag = form.pagamento.value;
  if (!pag) ok = false;
  if (pag === "Dinheiro" && !form.troco.value.trim()) {
    form.troco.classList.toggle("is-invalid", true);
    ok = false;
  } else {
    form.troco.classList.remove("is-invalid");
  }
  if (!ok) {
    toast("Preencha os dados da entrega");
    return;
  }

  const dados = {
    nome: form.nome.value.trim(),
    endereco: form.endereco.value.trim(),
    bairro: form.bairro.value.trim(),
    pagamento: pag,
    troco: form.troco.value.trim(),
    observacao: form.observacao.value.trim(),
  };
  const url = linkWhatsApp(montarMensagem(dados));
  window.open(url, "_blank", "noopener,noreferrer");
});

/* ----------------- init ----------------- */
function measureHeader() {
  const demo = document.querySelector(".demo-bar");
  const header = document.querySelector(".header");
  document.documentElement.style.setProperty("--demo-h", `${demo.offsetHeight}px`);
  document.documentElement.style.setProperty("--header-h", `${header.offsetHeight}px`);
}

document.getElementById("fab-wa").href = greetingLink();
renderHorario();
render();
syncTroco();
measureHeader();
window.addEventListener("resize", measureHeader);
setInterval(renderHorario, 60 * 1000);

window.__demo = { WHATSAPP_NUMBER, TAXA_ENTREGA, montarMensagem, linkWhatsApp, setQty, cart, cartEntries, subtotal, PRODUTOS, greetingLink };

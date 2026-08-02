# Vaz Power · Contexto do Projeto

Dashboards de tráfego pago (Google Ads + Meta Ads) para **Vaz Power Removals & Storage**
(Brisbane, AU), publicados no GitHub Pages. Gestor: **Fabricio Kaempf** (Kaempf Business).

## Preferências do Fabricio (seguir sempre)

- **FUSO HORÁRIO: sempre horário de Brasília (BRT, UTC-3).** Todo horário combinado,
  citado ou agendado é BR. O container roda em UTC, então ao usar CronCreate/agendamentos
  é preciso **somar 3 horas** (ex.: 18h BR = 21h UTC no cron). Nunca falar em UTC com ele.
- **Sem emoji com o cliente Vaz** (dashboards e mensagens de WhatsApp). Usar ícones SVG
  de linha (`stroke="currentColor"`). Símbolos geométricos (·, •, ▸, ★) são permitidos.
- **Sem travessão (em-dash)** em nenhum lugar. Usar "·", ":" ou vírgula; hífen para
  faixas e negativos.
- **Nunca usar "barato/barata"** nem variações. Falar em eficiência de CPL / custo por
  lead / de baixo valor.
- **Tom: nem formal, nem informal demais.** Evitar termos burocráticos como "do contrato"
  (usar "da operação", "do período", "até aqui") e também gírias.
- **Ações reais, nunca inventadas.** O bloco "Ação da semana" do dashboard descreve o que
  o Fabricio executou de fato: eu proponho um rascunho e ele valida antes de publicar.

## Publicação

- Repo `fabriciokaempf/VazPower`, branch padrão **`master`** (não main). Pages serve do
  master. Atualmente publicando **commit direto no master, sem PR**.
- **URL diferencia maiúsculas**: `https://fabriciokaempf.github.io/VazPower/<pasta>/`.
- Após publicar, o build "pages build and deployment" leva ~1 min. Se o cliente vir a
  versão antiga, é cache: Ctrl+Shift+R.

## Skills do projeto

- `metricas-trafego-2026` — playbook do dashboard semanal e comparativos.
- `google-ads-2026` — negativação de palavras-chave e qualificação de lead premium.

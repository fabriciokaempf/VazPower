# Vaz Power · Contexto do Projeto

Dashboards de tráfego pago (Google Ads + Meta Ads) para **Vaz Power Removals & Storage**
(Brisbane, AU), publicados no GitHub Pages. Gestor: **Fabricio Kaempf** (Kaempf Business).

> **Comece por `ESTADO.md`.** Ele traz o estado vivo da operação: próxima ação, histórico
> de métricas semana a semana, situação de cada campanha, pontos abertos e pendências.
> Este arquivo aqui guarda as regras que não mudam.

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

## Contexto operacional

- **Teto de orçamento vigente: ver `ESTADO.md`.** Em ago/2026 o cliente reduziu para
  A$2.500/semana por capacidade de atendimento reduzida, e em 24/08 decidiu encerrar
  o corte com a normalização do atendimento.
- Quando o cliente pedir redução, o critério é **menos volume com mais qualidade**:
  sacrificar as fontes de pior CPL e preservar as de melhor intenção (marca, ligações),
  nunca cortar proporcional. Na retomada, o caminho inverso: **devolver orçamento
  primeiro para o melhor custo**, e só depois para o que estiver fora do padrão.
- **No relatório:** variação de leads por decisão do cliente precisa aparecer como
  decisão, tanto na queda quanto na retomada, nunca como performance.

## Pendências combinadas

- **Fechamento de agosto/2026 (início de setembro): pedir os exports de PLATAFORMA e
  POSICIONAMENTO do Meta** (Facebook vs Instagram; Feed vs Stories vs Reels). Combinado
  em 03/08: o Fabricio puxa "só no mês que vem" e pediu para ser lembrado. Detalhes no
  skill `metricas-trafego-2026`.

## Skills do projeto

- `metricas-trafego-2026` — playbook do dashboard semanal e comparativos.
- `google-ads-2026` — negativação de palavras-chave e qualificação de lead premium.

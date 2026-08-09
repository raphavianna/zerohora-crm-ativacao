#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
inferir_genero.py — infere genero pelo PRIMEIRO NOME (PT-BR) e monta uma base de
email segmentada por sexo, respeitando consentimento de marketing (LGPD).

Uso tipico (base masculina para email mkt):
  python3 ativacao/inferir_genero.py \
      --in exports/clientes.utf8.csv --sexo M \
      --out exports/base_email_masculina.csv

Entrada: export de clientes da Nuvemshop (delimitador ';'). Se vier em ISO-8859-1,
converta antes:  iconv -f WINDOWS-1252 -t UTF-8 in.csv > in.utf8.csv
Colunas esperadas (nomes exatos do export): 'Nome completo', 'E-mail', 'Marketing'.

Consentimento: por padrao inclui so quem tem Marketing == 'Aceita' (opt-in do proprio
export). Use --sem-consentimento para ignorar o filtro (NAO recomendado para disparo).

PII: a saida contem nome/email — NUNCA versionar. Mantenha em exports/ (gitignored).

Metodo (nome e o unico sinal de sexo no export; nao ha coluna de sexo):
  1) dicionario curado de nomes masculinos/femininos BR;
  2) override para nomes que as regras erram;
  3) regras morfologicas (terminacao/sufixo) para a cauda longa;
  desconhecido/ambiguo -> 'U' (fora da base, por precisao). Rode --auditar para inspecionar.
"""
import csv, re, sys, argparse, unicodedata

def norm(s):
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z]', '', s.lower())


# --- Dicionarios e regras (auditados contra a base real) ---
MALE = set("""
joao jose antonio francisco carlos paulo pedro lucas luiz marcos luis gabriel rafael
daniel marcelo bruno eduardo felipe raimundo rodrigo manoel nelson roberto fabio
alexandre andre fernando leonardo mateus matheus vinicius gustavo guilherme thiago tiago
ricardo sergio joaquim mario davi david diego jorge sebastiao anderson julio cesar
igor arthur artur augusto benedito caio cauã caua cristiano danilo denis dennis douglas
elias emerson enzo everton ezequiel fabricio fellipe filipe geovane geovani geraldo
gilberto giovane henrique heitor hugo isaac italo ivan jackson jonas jean jefferson
joaquim juan kaua kauan kaique leandro levi lourival lucca luca luciano marcio mauricio
maycon michel miguel milton moacir moises murilo nathan nicolas noah otavio pablo
patrick reinaldo renan renato robson rogerio ronaldo ronaldinho ruan samuel saulo
sidney silvio simao tadeu tarcisio teodoro thales theo tomas ulisses valter walter
wagner wallace washington wellington wesley william willian wilson yago yan yuri
adriano aecio aguinaldo ailton alan alberto alcides aldair aldo alessandro alex alison
alvaro amauri amaury anael angelo aparecido aristeu arlindo aroldo baltazar bento
bernardo bradock bruce cassio cicero claudio cleber cleiton clovis conrado cristian
darlan delton demetrio dennys dionisio djalma domingos edenilson edgar edilson edinaldo
edison edmar edmilson edmundo ednaldo edson eduard edvaldo elber elder eliomar
elton emanuel emilio ernane ernesto esdras estevao ewerton fabiano ferdinando flavio
florentino francielo francinaldo frederico gilmar gilson gilvan giovani gledson godofredo
haroldo helio herculano heron hilton horacio idalberto ilan ismael israel ivo jaime
jair jairo jamerson jarbes jefte joel joelson johnny jonatas jonathan jonathas joni
josias josue jovino jucelino kelvin ladislau lauro lazaro lenilson leo leonan lindomar
lino livio lucio ludgero luidgi macario magno manuel marcelino marciano marcondes
mardem mariano marinaldo marlon martim martinho matias mauro maxwel maxwell messias
milton natanael natan neymar nilo nilson nilton noe norberto obede odair odilon
olavo olimpio orlando osmar osni osorio osvaldo oswaldo paulino peterson petrus
plinio pryscilla quintino rafhael railson ramon raul reginaldo remo ricar rian ricardo
rivaldo rivelino roberio robert roberval robinson rodolfo rogelio romario romerito
romildo romulo ronald roni ronivaldo ronny rosalvo rubem ruben rubens rui sadi sandro
santiago severino sidnei silas sivaldo solano tales talison teofilo tercio thadeu
theodoro tulio ubirajara urias uriel valdemar valdeci valdir valdomiro valentim
valmir vanderlei vanderson vicente vitor victor volnei wander wanderley wenderson
wendel wendell wesllei weslley wilker wilkerson yohan yohann zacarias zeca ademir
edgard ezio fabrizio gilmario ivanildo jadson jadir joabe joaozinho josimar josuel
juninho lelio marcus marlos marconi nataniel neto ney orestes ozeas pericles ramiro
raoni reis roldao romao ronei rosendo salomao sansao sinval tobias uilson vagner
valdeir valdinei vitorino wallison wanderlei welton weverton wiliam wilmar washingtom
adilson alceu alexssandro anisio arnaldo athila atila bendito bilo brayan breno
cassiano cauan celso chrystian claudinei cleiverson creuza cristovao damiao daniell
dario delcio denilson deusdedito edvan eliseu elizeu eliton emmanuel epaminondas
euclides eugenio euripedes evaldo evandro evilasio expedito fagner farley figueiredo
franklin gedeon gedeao geimison genario genesio getulio gideao gladson goncalo hebert
heberton helton hermes higor hiran hudson iago ianco isael ivair jamil jandir jarbas
joaocarlos jonhy jonhatan josenildo joseph jozimar kadu kaka keliton kennedy kenny
klebson kleber kleiton kleyton leandra lisandro loran lourenco lucemar luciamar
luizfernando luizhenrique manasses manolo marcelino mateuslucas moacyr murillo naldo
nazareno nelio nestor nickolas nikolas oberdan odilio olegario orivaldo osmarino
pio pyerre quintiliano rafhael rangel reginald rejane rennan reynaldo rildo rilton
rivaldo rjr robb roberley robinho rochester romilson ronaldi roosevelt rosivaldo
sabino saimon salvador sandoval savio schneider sebastian sergio setembrino sidcley
sildeney siloe silvano silverio silvestre simeao tarciano teixeira telmo tercio thulio
timoteo toninho tonny ualace ubaldo uendel ueslei valdenir valdiney valdo vanildo
vitorugo wadson waldeci waldemar waldir waldyr walison walmir walquer wanderly warley
washington wecsley wedson welbert weliton wellyngton welyngton weslei wesley westerley
whesley whodson wictor wilder wilmar winicius yohanes yuri zair zeus adao adan aderbal
adeilton adelio ademilson ademir adenilson aderaldo adhonias adivaldo admilson adnilson
adonias adonis adriel adrielson agostinho airton alairton alamir alanderson albari
""".split())

FEMALE = set("""
maria ana francisca antonia adriana juliana marcia fernanda patricia aline sandra
camila amanda bruna jessica leticia julia luciana vanessa mariana gabriela vera
vitoria laura bianca thais nathalia barbara carolina giovanna luana beatriz renata
luiza isabela sara caroline danielle isadora natalia nicole daniela brenda fabiana
monica debora eduarda livia rafaela roberta larissa jaqueline rosangela simone regina
angela silvia rita celia rose rosana rosa cristina claudia carla sonia sueli helena
teresa tereza cecilia lucia luzia elaine eliane elisangela eliana solange sofia
alessandra alice alessandandra alicia aparecida bruna carmen catia cintia cinthia
clarice cleide cristiane dandara dayane deise denise diana dirce dulce edna elenice
eliza elisa elisabete elisabeth emanuela emilly emily erica estela ester fatima
flavia gabrielly geovana gisele gislaine graziela heloisa iara ingrid isabel isabella
isis ivone jade jamile janaina jandira joana joice joyce jucelia kamila karen karina
karla katia kelly ketlin lais lara larisa layla lea leda leia lidia liliane lilian
lorena luana luciene lucimara ludmila luna madalena magda maiara maisa manuela mara
marcela margarida margarete mariah marlene marta martha maya melissa michele michelle
milena miriam mirian nadia nair natasha nayara neusa nilza noemi norma olivia pamela
paloma paola paula penelope poliana priscila priscilla rafaela raiane raissa raquel
rayane rebeca regiane renata rita rosangela roseli rosemeire rute sabrina samara
sandy sara selma sheila silvana socorro stefani stephanie tabata tais talita tamara
tania tatiana tatiane thainara thalita thamires thayna valentina valeria vania vera
veronica vilma virginia vitoria viviane wanda wilma yara yasmin zilda zuleide adelia
agatha agata alana alba alcione alda aldenora alessa aleteia alexia alexsandra
allana allison amabile amalia amelia analu andrea andreia andressa anelise anita
antonella arianne ariane barbara belinda benedita bernadete bruneli cacilda carina
carolayne cassia catarina celeste cibele cidinha clara claudete cleonice cleusa
consolata cristal dalva damaris darlene dayana debora deborah delfina detinha diana
dionara dorotea eduarda elza emanuelle emilene enedina eneida erika estefany eunice
euridice evelyn evelin fabiane fabricia fernandes gabriele giovana geovanna geralda
gilda giovanna gisele gislene gleice glaucia guiomar helloa hellen ianca iasmin
idalina ilza indianara ines ione irene iris isaura ivanete ivania jacira jaciara
jamila janete janaira jaqueline jenifer jennifer jeovana joanna jocelia jordana
josefa josiane josilene jovita jucineia juçara jucara kaila kailane kamile karol
karoline katiane keila kesia ketlyn kissila laila laisa lauriane leandra leidiane
leilane leonor leticia libia licia ligia lindalva lindaura lorayne lorna luara lucelia
luciana luci lucila lucinda ludmilla luisa luiza luma mabel macia madeleine mafalda
mailza malu manoela marcela mari mariangela marielly marilene marili marilia marina
marion marisa marise maristela marli marluce matilde maura mayara mayra meire melina
mercia meryelle micaela michaela milene mirela mirella nadir nara natalha neide
nicoly nilda nubia odete ohana ondina otavia palmira patricya perola pietra polyana
quiteria rafaella rafaela ramona raphaela rayssa regiane rejane renilda rhayssa riane
rosalia rosaria roseane roselaine roselia rosely rosemary roseni rosiane rosileia
rosilene rossana sabina safira salete samanta samantha sandy sarah sayonara scarlet
sebastiana selene selia sheyla shirley sirlene sirley solange soraia sueli suellen
suenia suzana suzane suzy sylvia tacia tainara tainah tamires tarcila tayla thabata
thaina thainara thalia thamara thassia thays thereza tuany ubiratan valeska valquiria
vanuza veridiana vilania virgilia vitoria walkiria wania wesla yandra yasmim zelia
zenaide zenilda zoraide zuila alzira aurora azenaide benta claricia cleidiane dircea
""".split())

# Override feminino: nomes que as regras morfologicas classificam errado como M
FEMALE_OVERRIDE = set("""
suelen izabel ellen helen vivian viviane kathleen caren karen carol carolzinha cleo
consuelo kellen kathelen glaucywellen gracyellen leydeellen helenir iasmim jasmim
iasmym iasmyn anaisabel liliam liliane margareth margaret nazareth merilyn meryellen
gladys goreth louise lourdes margot mayte nanci noeli sirlei rosy susy tays josy
gi gaby cacau munick ynae ysis wyne yone yessamin mire nathy jainny adrienni viviany
pryscilla priscilla creuza creusa rejane leandra luciamar rachel raquel yellen mikaelen
""".split())

# Lixo: fragmentos de email, sobrenomes soltos, marcadores de teste — nunca sao 1o nome
JUNK = set("""
anappoutlookcom cislanesousaflpgmailcom crisplantlabhotmailcom crisplantlab
coutinhojamile lucasde nuvemshop gomes andrade teste an li nao sem inalcicleide
cardoso daniell lucemar loran guiman henen deneo ramesten
""".split())

# Homens adicionais vistos na cauda (lista U) — false negatives a recuperar
MALE |= set("""
alef nicholas erick eric eryk erik herik herick ernandes giovanni giovani alexander
caue caua dimas durval dudu eder entony hagner hendrick jhimmy jhonny jhonatan john
johne juvenal kaike levy mark vini isaias eneas hyuri iury rycharles regis roger ruy
ruy walker willer thyerry thierri talef kesley kaike alef nickolas nikolas
""".split())

# Excecoes: nomes masculinos que terminam em 'a'
MALE_ENDS_A = set("""
luca nicola juca zeca dinha barnaba josua joshua elisha aba cha caua kaua joao
""".split())
# Excecoes: nomes femininos que terminam em 'o' / consoante masculina
FEMALE_ENDS_O = set("""
consolo socorro
""".split())

# Regras morfologicas (fallback quando fora do dicionario)
def rule(t):
    if len(t) < 2: return 'U'
    if t in MALE_ENDS_A: return 'M'
    if t in FEMALE_ENDS_O: return 'F'
    last = t[-1]
    if last == 'a': return 'F'
    if last == 'o': return 'M'
    # sufixos masculinos fortes
    if re.search(r'(son|ton|lton|zon|aldo|nando|berto|ilson|elson|ilton|inho|inildo|'
                 r'aldo|ismar|ilmar|almir|edro|iel|ael|uel|oel| air|eir|ir|or|ur|us|'
                 r'im|om|az|oz|ez|el|il|ol|ul|an|en|on|un|ram|dro|lho|ves|ico|ino|ero)$', t):
        return 'M'
    # sufixos femininos
    if re.search(r'(ete|ette|elly|ely|ily|elle|ele|ice|isse|ane|ene|ine|dis|lis|'
                 r'iz|mar|beth|ris)$', t):
        return 'F'
    return 'U'

def classify(t):
    if t in JUNK: return 'U'
    if t in FEMALE_OVERRIDE: return 'F'
    inM, inF = t in MALE, t in FEMALE
    if inM and inF: return 'AMB'
    if inM: return 'M'
    if inF: return 'F'
    return rule(t)  # 'M' | 'F' | 'U'


# --- CLI ---
COLS_SAIDA = ['Nome completo', 'E-mail', 'Telefone de Contato', 'Cidade', 'Estado',
              'Total Consumido (BRL)', 'Número de Compras', 'Última Compra']

def ler(path):
    # tenta utf-8; se falhar, cai para latin-1 (export cru da Nuvemshop)
    for enc in ('utf-8', 'latin-1'):
        try:
            with open(path, encoding=enc) as f:
                return list(csv.reader(f, delimiter=';'))
        except UnicodeDecodeError:
            continue
    raise SystemExit(f'nao consegui decodificar {path} (tente utf-8 ou latin-1)')

def main():
    ap = argparse.ArgumentParser(description='Infere sexo pelo 1o nome e monta base de email.')
    ap.add_argument('--in', dest='inp', required=True, help='CSV de clientes (delim ;)')
    ap.add_argument('--out', dest='out', help='CSV de saida (PII — nao versionar)')
    ap.add_argument('--sexo', choices=['M', 'F'], default='M', help='sexo a manter (default M)')
    ap.add_argument('--sem-consentimento', action='store_true',
                    help='ignora o filtro Marketing==Aceita (NAO recomendado p/ disparo)')
    ap.add_argument('--auditar', action='store_true',
                    help='imprime tokens por classe (M/F/U) p/ inspecao, nao grava base')
    a = ap.parse_args()

    linhas = ler(a.inp)
    if not linhas:
        raise SystemExit('arquivo vazio')
    header, data = linhas[0], linhas[1:]
    I = {h: i for i, h in enumerate(header)}
    obrig = ['Nome completo', 'E-mail']
    faltando = [c for c in obrig if c not in I]
    if faltando:
        raise SystemExit(f'colunas ausentes no export: {faltando}\nheader lido: {header}')
    def cel(row, k):
        i = I.get(k, -1)
        return row[i].strip() if 0 <= i < len(row) else ''

    if a.auditar:
        from collections import Counter
        by, tok = Counter(), {}
        for row in data:
            if not row or not cel(row, 'Nome completo'):
                continue
            g = classify(norm(cel(row, 'Nome completo').split()[0]))
            by[g] += 1
            tok.setdefault(g, Counter())[norm(cel(row, 'Nome completo').split()[0])] += 1
        print('distribuicao (por cliente):', dict(by))
        for g in ('M', 'F', 'U'):
            print(f'\n== {g} (top 40) ==')
            for n, c in tok.get(g, Counter()).most_common(40):
                print(f'  {c:3d} {n}')
        return

    tem_mkt = 'Marketing' in I
    vistos, base, sem_consent, sem_email = set(), [], 0, 0
    for row in data:
        nome = cel(row, 'Nome completo')
        if not nome:
            continue
        if classify(norm(nome.split()[0])) != a.sexo:
            continue
        email = cel(row, 'E-mail').lower()
        if '@' not in email:
            sem_email += 1
            continue
        if email in vistos:
            continue
        vistos.add(email)
        consent = (not tem_mkt) or (cel(row, 'Marketing') == 'Aceita')
        if not a.sem_consentimento and not consent:
            sem_consent += 1
            continue
        base.append(row)

    print(f'[base] sexo={a.sexo} · enviaveis={len(base)} · '
          f'suprimidos_sem_consentimento={sem_consent} · sem_email={sem_email}')

    if not a.out:
        print('(sem --out: nada gravado. Rode com --out exports/base.csv para salvar.)')
        return
    with open(a.out, 'w', newline='', encoding='utf-8') as o:
        w = csv.writer(o)
        cols = [c for c in COLS_SAIDA if c in I]
        w.writerow(['Primeiro nome'] + cols + ['Genero_inferido', 'Consentimento_mkt'])
        for row in base:
            primeiro = cel(row, 'Nome completo').split()[0].title()
            mkt = cel(row, 'Marketing') if tem_mkt else 'n/d'
            w.writerow([primeiro] + [cel(row, c) for c in cols] + [a.sexo, mkt])
    print(f'gravado: {a.out}  (PII — nao versionar)')

if __name__ == '__main__':
    main()

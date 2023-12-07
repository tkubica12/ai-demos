import os
from openai import AzureOpenAI
import time
import unidecode

# Set OpenAI API credentials
client = AzureOpenAI(
  api_key = os.environ['AZURE_OPENAI_API_KEY'],
  azure_endpoint = os.environ['OPENAI_URL'],
  api_version = "2023-09-01-preview",
)

deployment_name = os.getenv("DEPLOYMENT_NAME")

system_prompt = "Tvým úkolem je generovat otázky a odpovědi v prostředí fiktivní firmy TomSpace. Bude ti zadána nějaká oblast, například Jak tisknout, Výběr dovolené, Povinná školení, Vzdálené připojení, Objednávání kancelářských potřeb. V rámci této oblasti vygeneruj 30 otázek a odpovědí. Odpovědi ať jsou trochu vtipné a občas pro nějaké interní označení použij název obsahující slovo Tom, například TomTisk nebo TomObjednávky. Tady je příklad:\n\nOblast: Benefity\n\n<Tvůj výstup>\n\nOtázka: Jak zjistím, kolik je na mém účtu pro sportovní aktivity?\nOdpověď: Připoj se do systému TomSport a jdi do sekce Aktivity. Tam najdeš zůstatek svého účtu. A nezapomeň, že nevyčerpané body ti propadnou, takže je lepší pořádně zacvičit, než si jen ťukat do počítače a přijít o příspěvek\n\nOtázka: ...."

topics = [
    "Jak tisknout",
    "Výběr dovolené",
    "Povinná školení",
    "Vzdálené připojení",
    "Objednávání kancelářských potřeb",
    "Benefity",
    "Příspěvek na penzijní připojištění",
    "Podpora IT",
    "Ztráta průkazu",
    "Zapomenuté heslo",
    "Nefunkční počítač",
    "Nekvalitní káva",
    "Nefunkční klimatizace",
    "Problém s výtahem",
    "Právní poradenství",
    "Skartace dokumentů",
    "Výběr zdravotní pojišťovny",
    "Zaměstnanecké akcie",
    "Vzdělávání",
    "Zdravotní prohlídka",
    "Vánoční prázdniny",
    "Zpětná vazba",
    "Pracovní cesty",
]

sleep_time = 10

for topic in topics:     
    print(f"Generating {topic}")       
    message_text = [{"role":"system","content":system_prompt},{"role":"user","content":topic}]

    response = client.chat.completions.create(
        model=deployment_name,
        messages = message_text,
        temperature=0.7,
        max_tokens=7500,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    response_message = response.choices[0].message.content

    with open(f"{unidecode.unidecode(topic)}.txt", "w", encoding='utf-8') as f:
        f.write(response_message)

    print(f"Sleeping for {sleep_time} seconds")
    time.sleep(sleep_time)
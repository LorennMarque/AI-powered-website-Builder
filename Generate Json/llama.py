import replicate
import os
os.environ["REPLICATE_API_TOKEN"] = "r8_F4XY8ruDOI8lnO9UZe44Lmy4oHUw3a20Czwju"
# The meta/llama-2-7b-chat model can stream output as it's running.
for event in replicate.stream(
    "meta/llama-2-7b-chat",
    input={
        "prompt": "Hola! Como estas?",
        "system_prompt": "Eres un asistente que habla español"
    },
):
    print(str(event), end="")
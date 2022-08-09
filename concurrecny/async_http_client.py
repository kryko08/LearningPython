from aiohttp import ClientSession
import asyncio
import requests
import time


def sync_request(request_url):
    start_time = time.time()
    print(f"{sync_request.__name__} started running at {start_time}")

    # Collect pokemon cards!
    pokemon_data = []
    for card in range(1, 101):
        url = f"{request_url}/{card}"
        # send request individually for each pokemon
        res = requests.get(url)
        pokemon = res.json()
        pokemon_data.append(pokemon["name"])
    
    count = len(pokemon_data)
    total_time = time.time() - start_time
    print(f"{count} pokemons retrieved by {sync_request.__name__} in {total_time}")


async def async_request(request_url):
    start_time = time.time()
    print(f"{async_request.__name__} started running at {start_time}")
    
    pokemon_data = []
    async with ClientSession() as session:
        for card in range(1, 101):
            url = f"{request_url}/{card}"
            async with session.get(url) as resp:
                # Still awaiting response
                pokemon = await resp.json()
                pokemon_data.append(pokemon["name"])
    
    count = len(pokemon_data)
    total_time = time.time() - start_time
    print(f"{count} pokemons retrieved by {async_request.__name__} in {total_time}")


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon_data = await resp.json()
        return pokemon_data["name"]


async def async_request_update(request_url):
    start_time = time.time()
    print(f"{async_request_update.__name__} started running at {start_time}")

    actions = []
    pokemon_data = []
    async with ClientSession() as session:
        for card in range(1, 101):
            url = f"{request_url}/{card}"
            actions.append(asyncio.create_task(get_pokemon(session, url)))

        pokemon_res = await asyncio.gather(*actions)
        for data in pokemon_res:
            pokemon_data.append(data)

    count = len(pokemon_data)
    total_time = time.time() - start_time
    print(f"{count} pokemons retrieved by {async_request_update.__name__} in {total_time}")


# sync_request("https://pokeapi.co/api/v2/pokemon")
# asyncio.run(async_request("https://pokeapi.co/api/v2/pokemon"))
asyncio.run(async_request_update("https://pokeapi.co/api/v2/pokemon"))





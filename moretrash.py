import asyncio
 
async def foo():
    print("Start foo")
    await asyncio.sleep(1)
    print("End foo")
 
async def bar():
    print("Start bar")
    await asyncio.sleep(2)
    print("End bar")
 
async def main():
    await asyncio.gather(foo(), bar())
 
asyncio.run(main())
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
import asyncio

# MONGO_URI = "mongodb://bigsauto:526892@0.0.0.0:27017/ba_db?authSource=admin"
MONGO_URI = "mongodb://bigsauto:526892@0.0.0.0:27017/ba_db"


client = AsyncIOMotorClient(MONGO_URI)

db = client.ba_db
collection: AsyncIOMotorCollection = db.test

async def insert_and_verify():
    # Insert test data
    test_data = {"name": "John Doe", "age": 30}
    result = await collection.insert_one(test_data)
    print(f"Inserted document with ID: {result.inserted_id}")

    # Retrieve the inserted data to verify
    document = await collection.find_one({"_id": result.inserted_id})
    print("Retrieved document:", document)


if __name__ == "__main__":
    # Run the test
    asyncio.run(insert_and_verify())


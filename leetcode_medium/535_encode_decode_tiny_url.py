

class Bucket:
    def __init__(self):
        self.value_map = {}
        self.counter = 0

    def encode(self, url: str, bucket_id: int):
        key = f"{bucket_id}_{self.counter}"
        self.value_map[key] = url
        self.counter += 1
        return key

    def decode(self, bucket_id, counter_id):
        key = f"{bucket_id}_{counter_id}"
        return self.value_map[key]


class Codec:

    def __init__(self):
        self.buckets = [None] * 100_000

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        bucket_id = hash(longUrl) % len(self.buckets)
        if self.buckets[bucket_id] is None:
            b = Bucket()
            self.buckets[bucket_id] = b
            val = b.encode(longUrl, bucket_id)
            return val
        else:
            b = self.buckets[bucket_id]
            val = b.encode(longUrl, bucket_id)
            return val

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        bucket_id, item_id = shortUrl.split('_')
        bucket_id = int(bucket_id)
        item_id = int(item_id)
        b = self.buckets[bucket_id]
        return b.decode(bucket_id, item_id)
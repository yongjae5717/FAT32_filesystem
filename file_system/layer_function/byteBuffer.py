from struct import *


class ByteBuffer:
    def __init__(self, bs):
        self.m_data = bs
        self.m_offset = 0
        self.m_limit = len(bs)

    def size(self):
        return len(self.m_data)

    def limit(self):
        return len(self.m_data)

    def offset(self):
        return self.m_offset

    def jump(self, n):
        self.m_offset += n

    def get_uint2_be(self):
        s = self.m_offset
        r = self.m_data[s:s+2]
        self.m_offset += 2

        return unpack('>H', r)[0]

    def get_uint2_le(self):
        s = self.m_offset
        r = self.m_data[s:s+2]
        self.m_offset += 2

        return unpack('<H', r)[0]

    def get_uint4_be(self):
        s = self.m_offset
        r = self.m_data[s:s+4]
        self.m_offset += 4

        return unpack('>I', r)[0]

    def get_uint4_le(self):
        s = self.m_offset
        r = self.m_data[s:s+4]
        self.m_offset += 4

        return unpack('<I', r)[0]

    def get_data2(self):
        s = self.m_offset
        r = self.m_data[s:s+2]
        self.m_offset += 2
        return r

    def get_ascii(self, index):
        # index = self.m_data.find(b'\x00', self.m_offset)
        if index == -1:
            self.m_offset = self.m_limit
            return self.m_data[self.m_offset:].decode('latin-1').encode("utf-8").decode('utf-8').strip()

        res = self.m_data[self.m_offset:self.m_offset + index].decode('latin-1').encode("utf-8").decode('utf-8').strip()
        self.m_offset += index

        return res

    def get_utf16_le(self, size):
        o = self.m_offset
        res = self.m_data[o:o+size*2].decode('utf-16le')
        self.m_offset += size*2

        return res

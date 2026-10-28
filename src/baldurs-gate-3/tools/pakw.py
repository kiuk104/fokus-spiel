"""LSPK v18 쓰기 (LZ4 압축)"""
import struct, sys, os, lz4.block
def write(root, out):
    files = []
    for dp, _, fs in os.walk(root):
        for f in fs:
            p = os.path.join(dp, f); files.append((os.path.relpath(p, root).replace(os.sep, '/'), open(p, 'rb').read()))
    data = b''; ents = b''; off = 40
    for name, raw in files:
        c = lz4.block.compress(raw, store_size=False)
        nb = name.encode('utf-8'); assert len(nb) < 256
        ents += nb.ljust(256, b'\0') + struct.pack('<IHBBII', off & 0xFFFFFFFF, off >> 32, 0, 0x2, len(c), len(raw))
        data += c; off += len(c)
    lst = lz4.block.compress(ents, store_size=False)
    flo = 40 + len(data)
    hdr = b'LSPK' + struct.pack('<IQIBB16sH', 18, flo, len(lst) + 8, 0, 0, b'\0' * 16, 1)
    assert len(hdr) == 40
    open(out, 'wb').write(hdr + data + struct.pack('<II', len(files), len(lst)) + lst)
    print(out, len(files), 'files', os.path.getsize(out), 'bytes')
write(sys.argv[1], sys.argv[2])

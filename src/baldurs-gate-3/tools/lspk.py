import struct, sys, os, lz4.block, zlib
def read(path, out):
    f=open(path,'rb'); d=f.read()
    assert d[:4]==b'LSPK', d[:4]
    ver,=struct.unpack_from('<I',d,4); flo,fls=struct.unpack_from('<QI',d,8)
    n,cs=struct.unpack_from('<II',d,flo)
    lst=lz4.block.decompress(d[flo+8:flo+8+cs],uncompressed_size=n*272)
    for i in range(n):
        e=lst[i*272:(i+1)*272]
        name=e[:256].split(b'\0')[0].decode()
        o1,o2,part,fl,sod,us=struct.unpack_from('<IHBBII',e,256)
        off=o1|(o2<<32); raw=d[off:off+sod]; m=fl&0xF
        data=raw if m==0 else (zlib.decompress(raw) if m==1 else lz4.block.decompress(raw,uncompressed_size=us) if m==2 else __import__('zstandard').ZstdDecompressor().decompress(raw,max_output_size=us))
        p=os.path.join(out,name); os.makedirs(os.path.dirname(p),exist_ok=True); open(p,'wb').write(data)
        print(ver,name,us)
read(sys.argv[1],sys.argv[2])

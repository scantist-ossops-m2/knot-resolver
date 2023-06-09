"""
This type stub file was generated by pyright.
"""

RCS_ID = ...
class simple_producer:
    """producer for a string"""
    def __init__(self, data, buffer_size=...) -> None:
        ...
    
    def more(self): # -> bytes | Unknown:
        ...
    


class scanning_producer:
    """like simple_producer, but more efficient for large strings"""
    def __init__(self, data, buffer_size=...) -> None:
        ...
    
    def more(self): # -> Literal[b'']:
        ...
    


class lines_producer:
    """producer for a list of lines"""
    def __init__(self, lines) -> None:
        ...
    
    def more(self): # -> str:
        ...
    


class buffer_list_producer:
    """producer for a list of strings"""
    def __init__(self, buffers) -> None:
        ...
    
    def more(self): # -> Literal[b'']:
        ...
    


class file_producer:
    """producer wrapper for file[-like] objects"""
    out_buffer_size = ...
    def __init__(self, file) -> None:
        ...
    
    def more(self): # -> Literal[b'']:
        ...
    


class output_producer:
    """Acts like an output file; suitable for capturing sys.stdout"""
    def __init__(self) -> None:
        ...
    
    def write(self, data): # -> None:
        ...
    
    def writeline(self, line): # -> None:
        ...
    
    def writelines(self, lines): # -> None:
        ...
    
    def flush(self): # -> None:
        ...
    
    def softspace(self, *args): # -> None:
        ...
    
    def more(self): # -> bytes | Literal['']:
        ...
    


class composite_producer:
    """combine a fifo of producers into one"""
    def __init__(self, producers) -> None:
        ...
    
    def more(self): # -> Literal[b'']:
        ...
    


class globbing_producer:
    """
    'glob' the output from a producer into a particular buffer size.
    helps reduce the number of calls to send().  [this appears to
    gain about 30% performance on requests to a single channel]
    """
    def __init__(self, producer, buffer_size=...) -> None:
        ...
    
    def more(self): # -> bytes:
        ...
    


class hooked_producer:
    """
    A producer that will call <function> when it empties,.
    with an argument of the number of bytes produced.  Useful
    for logging/instrumentation purposes.
    """
    def __init__(self, producer, function) -> None:
        ...
    
    def more(self): # -> Literal['']:
        ...
    


class chunked_producer:
    """A producer that implements the 'chunked' transfer coding for HTTP/1.1.
    Here is a sample usage:
            request['Transfer-Encoding'] = 'chunked'
            request.push (
                    producers.chunked_producer (your_producer)
                    )
            request.done()
    """
    def __init__(self, producer, footers=...) -> None:
        ...
    
    def more(self): # -> bytes:
        ...
    


class compressed_producer:
    """
    Compress another producer on-the-fly, using ZLIB
    """
    def __init__(self, producer, level=...) -> None:
        ...
    
    def more(self): # -> bytes:
        ...
    


class escaping_producer:
    """A producer that escapes a sequence of characters"""
    def __init__(self, producer, esc_from=..., esc_to=...) -> None:
        ...
    
    def more(self):
        ...

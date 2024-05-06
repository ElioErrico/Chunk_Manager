from cat.mad_hatter.decorators import hook

@hook
def rabbithole_instantiates_splitter(text_splitter, cat):
    
    settings = cat.mad_hatter.plugins["ccat_chunk_manager"].load_settings()
    edited_chunk_size = settings["Chunk_Size"]
    edited_chunk_overlap = settings["Chunk_Overlap"]

    # example on how to change chunking
    text_splitter._chunk_size = edited_chunk_size
    text_splitter._chunk_overlap = edited_chunk_overlap

    return text_splitter
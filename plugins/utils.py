import re

def parse_grammar(text, question: bool = False):
    # 1. Clean up spacing around punctuation so matching works accurately
    text = re.sub(r'\s*\?\s*$', '', text.strip())
    
    # 2. Define word lists using regex word boundaries (\b)
    wh_pattern = r'\b(What kind of|What|Who|Where|When|Why|How|Which|Whose|Que tipo de|Qué|Quién|Dónde|Cuándo|Por qué|Cómo|Cuál|De quién)\b'
    be_pattern = r'\b(are|is|am|was|were|soy|es|eres|somos|son|estoy|estás|está|estamos|están)\b'
    auxiliaries_pattern = r'\b(going to|did|do|does|have|has)\b'
    pronoun_pattern = r'\b(you|i|he|she|it|we|they|yo|tú|él|ella|nosotros|ellos)\b'
    
    # CRITICAL FIX: Ensure the verb is NOT inside an already processed {...} tag
    # (?![^[:*\]]*\]) guarantees we aren't matching inside the color brackets like [red] or [blue]
    # To keep it simple and robust, we use a negative lookahead/lookbehind strategy or match untagged words.
    
    verb_list = (
        r'eat|ate|eaten|eating|drink|drank|drunk|drinking|read|reading|write|wrote|written|writing|'
        r'watch|watched|watching|call|called|calling|take|took|taken|taking|give|gave|given|giving|'
        r'buy|bought|buying|sell|sold|selling|open|opened|opening|close|closed|closing|listen to|'
        r'listened to|listening to|go|went|gone|going|come|came|coming|sit|sat|sitting|stand|stood|'
        r'standing|cook|cooked|cooking|ask|asked|asking|play|played|playing|tell|told|telling|'
        r'work|worked|working|repair|repaired|repairing|study|studied|studying|bring|brought|'
        r'bringing|pick up|picked up|picking up|put|putting|meet|met|meeting|drive|drove|driven|'
        r'driving|dance|danced|dancing|want|wanted|wanting|know|knew|known|knowing|teach|taught|'
        r'teaching|visit|visited|visiting|think|thought|thinking|like|liked|liking|plan|planned|'
        r'planning|travel|traveled|traveling|talk|talked|talking|need|needed|needing|make|made|'
        r'making|do|did|done|doing|sing|sang|sung|singing|walk|walked|walking|feel|felt|feeling|'
        r'cut|cutting|have|had|having|sleep|slept|sleeping|send|sent|sending|run|ran|running|'
        r'see|saw|seen|seeing|wear|wore|worn|wearing|lie|lied|lying|argue|argued|arguing|'
        r'help|helped|helping|pay|paid|paying'
    )
    
    # 3. Apply replacements in strict order
    text = re.sub(wh_pattern, r'<span class="grammar-teal">\1</span>', text, flags=re.IGNORECASE)
    text = re.sub(be_pattern, r'<span class="grammar-pink">\1</span>', text, flags=re.IGNORECASE)
    text = re.sub(auxiliaries_pattern, r'<span class="grammar-red">\1</span>', text, flags=re.IGNORECASE)
    text = re.sub(pronoun_pattern, r'<span class="grammar-green">\1</span>', text, flags=re.IGNORECASE)
    
    # THE SECRET SAUCE: 
    # This regex matches an already tagged block (*SKIP)(*FAIL) OR your untagged action verbs.
    # It completely prevents touching words inside {...}[color]
    protection_pattern = r'\{[^}]+\}\[[^\]]+\]|<span\b[^>]*>.*?</span>'
    final_verb_pattern = rf'{protection_pattern}|(?:\b({verb_list})\b)'
    
    text = re.sub(final_verb_pattern, lambda m: m.group(0) if m.group(1) is None else f'<span class="grammar-blue">{m.group(1)}</span>', text, flags=re.IGNORECASE)
    
    # 4. Put the question mark back at the very end
    text = f"{text}?" if question else text
    return f"<div class='grammar'>{text}</div>"
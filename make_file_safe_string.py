"""
Url: https://gist.github.com/wassname/1393c4a57cfcbf03641dbc31886123b8
"""

import re
import string

import unicodedata

valid_filename_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
"""
str: A string containing all of the valid filename characters.
"""
char_limit = 255
"""
int: The maximumn number of characters allowed for a filename in Windows (255).
"""


def _replace_spaces_with_underscores(filename, replace=' '):
    """
    Replace all of the spaces (` `) in a filename with underscores (`_`).

    Parameters
    ----------
    filename : str
        A string that needs the spaces (` `) converted into underscores (`_`).
    replace : str
        The string character to replace in the filename with `_`. By default, this will be spaces.

    Returns
    -------
    str
        By default, a copy of `filename` without any spaces. It will only have underscores.
        Setting the `replace` parameter will change what character is removed.
    """
    for r in replace:
        filename = filename.replace(r, '_')
    return filename


def _preserve_valid_ascii_character(filename):
    """
    Return a filename string that contains only valid ASCII characters.

    Parameters
    ----------
    filename : str
        A string that needs only valid ASCII characters.

    Returns
    -------
    str
        A copy of `filename` with only valid ASCII characters.
    """
    return unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()


def _remove_extra_whitespaces(filename):
    """
    Remove any extra whitespaces around the filename string.
    
    Parameters
    ----------
    filename : str
        A string I want to strip the whitespace off of.

    Returns
    -------
    str
        A copy of `filename` without any extra whitespaces.
    """
    filename = filename.strip()
    return re.sub('\s+', ' ', filename)


def _preserve_whitelisted_characters(cleaned_filename, whitelist=valid_filename_chars):
    """
    Preserve whitelisted characters in the filename.
    Truncate the filename to the first 256 characters.
    
    Parameters
    ----------
    cleaned_filename : str
        The pre-processed filename.
    whitelist : str
        A string containing all the valid characters.
    
    Returns
    -------
    str
        The final filename.
    """
    cleaned_filename = ''.join(c for c in cleaned_filename if c in whitelist)
    if len(cleaned_filename) > char_limit:
        print(
            "Warning, filename truncated because it was over {}. Filenames may no longer be unique".format(char_limit))
    return cleaned_filename[:char_limit]


def clean_filename(filename, whitelist=valid_filename_chars, replace=' '):
    """
    Create a clean filename.
    
    Parameters
    ----------
    filename : str
        The initial "dirty" filename.
    whitelist : str
        A string containing all the whitelisted characters.
    replace : str
        By default, space.
        
    Returns
    -------
    str
        The final clean filename.
    """
    dirty_filename = _replace_spaces_with_underscores(filename, replace)
    compressed_filename = _remove_extra_whitespaces(dirty_filename)
    cleaner_filename = _preserve_valid_ascii_character(compressed_filename)
    return _preserve_whitelisted_characters(cleaner_filename, whitelist)

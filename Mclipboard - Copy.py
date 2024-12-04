import argparse, pyperclip, shelve
from List_String import List_to_String as stg
from Apostrophe import apostrophe as apos

def direct():

    """
    Parse command-line arguments and return the action and keyword(s).

    Returns:
        tuple: A tuple containing the command and a list of keywords.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices = ['save', 'get', 'list', 'delete', 'deleteall'])
    parser.add_argument('keyword', nargs = '*')
    arg = parser.parse_args()
    return arg.command, arg.keyword

def multi_clip(action = '', keyphrase = ''):

    """
    Perform actions on a multi-clipboard storage system based on the specified action and keyphrases.

    Args:
        action (str): The action to perform (save, get, list, delete, deleteall).
        keyphrase (list or str): The keyphrase(s) related to the action.

    Raises:
        Exception: If the action is invalid or keyphrase is not in the correct format.
    """

    if __name__ != "__main__":
        choice = ['save', 'get', 'list', 'delete', 'deleteall']
        if action not in choice :
            raise Exception(f"operation can only be one of: {stg(choice)}")
        if  not isinstance(keyphrase, list):
            keyphrase = [keyphrase]

    # Clipboard content and storage setup
    clip = pyperclip.paste()
    store = shelve.open('ClipboardFile')
    new = []
    save = {}
    deleted = []

    # Handling 'save' operation
    if action.lower() == 'save' and len(keyphrase) == 1:
        store[keyphrase[0].lower()] = clip
        print(f"Saved to the Multi-Clipboard: '{keyphrase[0]}'")
    elif action.lower() == 'save' and len(keyphrase) > 1:
        split_clip = clip.split('\n')
        if len(split_clip) == len(keyphrase):
            for i, j in enumerate(keyphrase):
                store[j.lower()] = split_clip[i]
                new.append(j)
            print(f'Saved to the Multi-Clipboard line by line: {apos(stg(new))}')
        if len(split_clip) > len(keyphrase):
            for i, j in enumerate(keyphrase):
                store[j.lower()] = split_clip[i]
                new.append(split_clip[i])
            not_save = split_clip[len(new):]
            print(f'Saved to the Multi-Clipboard line by line: {apos(stg(new))}\
            \nNo enough keyphrases to be saved to: {apos(stg(not_save))}\
            \nYou can input the keyphrase(s) one after the other')
            for i, j in enumerate(not_save):
                key = input()
                if key != '':
                    store[key.lower()] = j
                    save[key] = j
                else:
                    deleted.append(not_save.pop(i))
            print(f"Saved to the Multi-Clipboard: {list(save.values())} to {list(save.keys())}\
            accordingly\nDeleted: {deleted}")
        if len(split_clip) < len(keyphrase):
            for i, j in enumerate(split_clip):
                store[keyphrase[i].lower()] = j
                new.append(keyphrase[i])
            not_save = keyphrase[len(new):]
            print(f'Saved to the Multi-Clipboard line by line: {apos(stg(new))}\
            \nNo enough content lines for to be saved: {apos(stg(not_save))}\
            \nYou can input the content(s) one after the other')
            for i, j in enumerate(not_save):
                content = input()
                if content != '':
                    store[j.lower()] = content
                    save[j] = content
                else:
                    deleted.append(not_save.pop(i))
            print(f"Saved to the Multi-Clipboard: {list(save.values())} to {list(save.keys())}\
            accordingly\nDeleted: {deleted}")

    # Handling 'get' operation
    elif action == 'get' and len(keyphrase) == 1:
        if keyphrase[0].lower() in store:
            pyperclip.copy(store[keyphrase[0].lower()])
            print(f"Copied to the clipboard: Content of keyphrase {keyphrase[0]}")
        else:
            print(f"{keyphrase} not found in the multiclipboard -- You can input content for it")
            content = input()
            if content != '':
                store[keyphrase[0].lower()] = content
                pyperclip.copy(content)
                print(f"Your input for {keyphrase} -- Saved and Copied to the clipboard")
    elif action == 'get' and len(keyphrase) > 1:
        clipboard = []
        for i, j in enumerate(keyphrase):
            if j.lower() in store:
                clipboard.append(store[j.lower()])
            else:
                print(f"'{j}' not found in the multiclipboard -- You can input content for it")
                content = input()
                if content == '':
                    continue
                else:
                    store[j.lower()] = content
                    clipboard.append(content)
        clipboards = '\n\n'.join(clipboard)
        pyperclip.copy(clipboards)

    # Handling 'list' operation
    elif action.lower() == 'list':
        if list(store.keys()) != []:
            pyperclip.copy('All keyphrases in the Multi-Clipboard:' + apos(stg(list(store.keys()))))
            print('All keyphrases in the Multi-Clipboard copied to the clipboard:' + apos(stg(list(store.keys()))))
        else:
            print('The Multiclipboard Empty -- No keyphrase or content found')

    # Handling 'delete' operation
    elif action.lower() == 'delete' and len(keyphrase) == 1:
        if keyphrase[0].lower() in store:
            del store[keyphrase[0].lower()]
            print(f"Deleted from the multiclipboard: '{keyphrase[0]}'")
        else:
            print(f"'{keyphrase[0]}' not in the multiclipboard already")
    elif action.lower() == 'delete' and len(keyphrase) > 1:
        for i, j in enumerate(keyphrase):
            if j.lower() in store:
                delete = store.pop(j.lower())
                deleted.append(delete)
            else:
                new.append(j)
        if deleted != [] and new != []:
            print(f"Deleted from the multiclipboard: {deleted}\n{new} not in the multiclipboard already")
        elif deleted != [] and new == []:
            print(f"Deleted from the multiclipboard: {deleted}")
        elif deleted == [] and new != []:
            print(f'{new} not in the multiclipboard already')

    # Handling 'deleteall' operation
    elif action.lower() == 'deleteall':
        for i, j in enumerate(store):
            del store[j]
        print('Delete All -- The multiclipboard totally cleared')
    store.close()

if __name__ ==  '__main__':
    #Entry point for the program. Parses arguments and performs the specified action.
    command, keyword = direct()
    multi_clip(command, keyword)

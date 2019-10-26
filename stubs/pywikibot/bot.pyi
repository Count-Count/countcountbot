from typing import Iterable, Optional
import pywikibot

class SingleSiteBot:
    _generator_completed: bool
    def __init__(self, site: pywikibot.site.BaseSite) -> None: ...
    @property
    def site(self) -> pywikibot.site.BaseSite: ...
    def skip_page(self, page: pywikibot.Page) -> bool: ...
    def run(self) -> None: ...
    def exit(self) -> None: ...

def handle_args(args: Optional[Iterable[str]] = None, do_help: bool = True) -> Iterable[str]: ...
# -*- coding: utf-8 -*-
import os
import re
import time
from typing import Union, List

import deepl

from videotrans.configure import config
from videotrans.translator._base import BaseTrans
from videotrans.util import tools

class DeepL(BaseTrans):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.api_url=None if not config.params['deepl_api'] else config.params['deepl_api'].rstrip('/')

        pro = self._set_proxy(type='set')
        if pro:
            self.proxies = {"https": pro, "http": pro}

    def _item_task(self,data:Union[List[str],str]) ->str:
        deepltranslator = deepl.Translator(config.params['deepl_authkey'],server_url=self.api_url,proxy=self.proxies)
        config.logger.info(f'[DeepL]请求数据:{data=},{config.params["deepl_gid"]=}')

        result = deepltranslator.translate_text(
            "\n".join(data),
            source_lang=self.source_code.upper()[:2] if self.source_code else None,
            target_lang='EN-US' if self.target_language == 'EN' else self.target_language,
            glossary=config.params['deepl_gid'] if config.params['deepl_gid'] else None
        )

        config.logger.info(f'[DeepL]返回:{result=}')
        return result.text
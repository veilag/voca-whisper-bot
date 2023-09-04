from aiogram import Router
from .dialog import dialog

router: Router = Router()
router.include_router(dialog)

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import sympy

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    polinom1 = sympy.polys.polytools.poly_from_expr(str(items[1]))[0]
    polinom2 = sympy.polys.polytools.poly_from_expr(str(items[2]))[0]
    sumPolinom = str((polinom1+polinom2).as_expr()).replace('**','^')+' = 0'    
    await update.message.reply_text(f'Сумма полиномов:\n {sumPolinom}')

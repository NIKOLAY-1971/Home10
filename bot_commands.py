from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    k = int(items[1])
 
    lst = []
    lstNew = []
    for i in range(k+1):
        lst.append(random.randint(0, 100))
    for i in lst:
        if i:
            if k == 0:
                variable = ''
            elif k == 1:
                variable = 'x'
            else:
                variable = f'x^{k}'
            variable_k = f'{i}{variable}'
            lstNew.append(variable_k)
        k = k-1
    polinom = '+'.join(lstNew)+'=0'
        
    await update.message.reply_text(f'Полином:\n {polinom}')

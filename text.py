async def msg(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Обработчик команды /msg для администратора."""
        # Проверяем, что команда вызвана в личных сообщениях
        if update.effective_chat.type != ChatType.PRIVATE:
            return

        # Проверяем, что пользователь является администратором
        user_id = update.effective_user.id
        if not is_admin(user_id):
            await update.message.reply_text("❌ У вас нет прав для выполнения этой команды.")
            return

        # Получаем текст сообщения из аргументов команды
        if not context.args:
            await update.message.reply_text(
                "❌ Использование: /msg текст сообщения\n"
                "Пример: /msg Важное объявление"
            )
            return

        # Объединяем все аргументы в одно сообщение
        message_text = " ".join(context.args)

        # Отправляем сообщение в группу в тот же тред, куда отправляется расписание
        from src.utils.secrets import GROUP_ID, SCHEDULE_THREAD_ID

        try:
            try:
                # Пытаемся отправить в тред (как в daily_schedule_service)
                await context.bot.send_message(
                    chat_id=GROUP_ID,
                    text=message_text,
                    message_thread_id=SCHEDULE_THREAD_ID
                )
                await update.message.reply_text("✅ Сообщение успешно отправлено в группу.")
            except Exception:
                # Если не удалось отправить в тред, отправляем без указания треда
                await context.bot.send_message(
                    chat_id=GROUP_ID,
                    text=message_text
                )
                await update.message.reply_text("✅ Сообщение успешно отправлено в группу.")
        except Exception as e:
            await update.message.reply_text(f"❌ Ошибка при отправке сообщения: {e}")

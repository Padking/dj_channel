from django import forms


class ChannelForm(forms.Form):
    ch = forms.CharField(
                        label="Telegram-каналы",
                        help_text= """
                                <i><u>Заполните в формате:</u></i><br>
                                        имя канала 1<br>
                                        имя канала 2<br>
                                        и т.д.
                                    """,
                        max_length=64, required=False,
                        widget=forms.Textarea
                        )

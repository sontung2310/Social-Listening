from steamship import Steamship
with open('prompt_key.txt', 'r', encoding='utf-8') as file:
    prompt_mn = file.read().rstrip()
input_text = "HIGHLIGHTS: NANTES - JUVENTUS | THẺ ĐỎ NGỚ NGẨN, DI MARIA LẬP HAT-TRICK ĐẲNG CẤP | UEL 22/23"
prompt = "Act as you are document key information extraction model. Trích xuất từ khóa chính trong nội dung sau, nếu không có từ khóa nào thì trả lời 'None':.\n" + prompt_mn + "\nText '''{}'''\nKey Information: ".format(input_text)
# print(prompt)
# resp = api.send_message(prompt)
# print(resp['message'])

client = Steamship(api_key='341FEFC8-681E-4A8D-BFC9-6C6A4C4F097A',workspace="gpt-4")

# Create an instance of this generator
generator = client.use_plugin('gpt-4')
# Generate text
task = generator.generate(text=prompt)

# Wait for completion of the task.
task.wait()

# Print the output
print(task.output.blocks[0].text)
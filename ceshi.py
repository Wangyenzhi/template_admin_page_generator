from dcb_admin_page_generator.main import *


if __name__ == '__main__':
    from config import defineConfig as temp_cfg
    target_file_path = input('输入生成目标路径(不填生成在当前根页面)')
    page_title = input('请输入生成页面标题(必填)')
    page_type = input('请输入想要生成的Page Type(1、list 2、add 3、dialog_list 4、dialog_add)')
    my_generator = generator(temp_cfg, page_title, page_type, '')
    with open(f'{target_file_path + "/" if target_file_path else ""}{page_type}.vue', 'w', encoding='utf8') as f:
        f.write(my_generator.generate())

from dcb_admin_page_generator.main import *


if __name__ == '__main__':
    from dcb_admin_generator_config import defineConfig as temp_cfg
    target_file_path = input('输入生成目标路径(不填生成在当前根页面)')
    my_generator = generator(temp_cfg,target_file_path)
    with open(f'{target_file_path + "/" if target_file_path else ""}list.vue', 'w', encoding='utf8') as f:
        f.write(my_generator.generate())

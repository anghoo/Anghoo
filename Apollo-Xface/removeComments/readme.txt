apollo发布时去掉工程里面的一些文件夹与文件，去掉java文件的注释,现支持的注释：
	a./*
	   *
	   */
	b./*.....*/
	c.//
用法： xFacePublish.py apollo_dir target_dir

    如果apollo_dir 路径不存在，则出错，target_dir可以不存在，但是盘符一定要存在

	apollo_dir: apollo源码的目录（到produc目录），例如：“E:/xface 3.0/xface3.0_guopc_PC-201106091514_35/trunk/product”
	target_dir: 最后去掉不需要发布的文件与注释的源码目录，例如： “E:/apolloPublish”





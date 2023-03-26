@pytest.mark:
	Test işlemlerinde meta veriler eklemeye yarar.
	@pytest.mark.parametrize:
		Aynı testi farklı parametreler ile yapmaya yarar. Parametre adları ve değerleri bağımsız değişkenler olabilir.
		@pytest.mark.parametrize("x,y", [(1, 2), (3, 4)])
	@pytest.mark.usefixtures:
		Bir ya da birden fazla fixture için açıkça argüman olarak iletmeden kullanmaya yarar.
		@pytest.mark.usefixtures("some_fixture")
	@pytest.mark.skipif:
		Belirli bir koşul sağlandığında testi veya sınıfı atlamaya yarar. Koşul bağımsız değişken olabilir.
		@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
	@pytest.mark.skip:
		Koşulsuz olarak atlamaya yarar. 
		@pytest.mark.skip(reason="pass")
	@pytest.mark.xfail
		testin hatalı olmasının beklediğini söyler
		@pytest.xfail(reason="bug")
			Hatannın sebebini açıklar
		@pytest.xfail(strict=True)
			Parametre testlerinin daha sıkı kontrol edilmesini sağlar. Test edilmek isteden davarınışın gerçekten test ediliğinden emin olunmak için kullanılır. 
		@pytest.xfail(run=False)
			Çalıştırılmasını engeller. Özellikle yorumlayıcıyı çökerten xfailing testlerine kullanışlıdır.

import timeit
from rabin_karp_search import rabin_karp_search
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search


def read_file(file_path):
	with open(file_path, 'r', encoding='utf-8') as file:
		text = file.read()
	return text


def measure_algorithm(algorithm, text, pattern):
	start_time = timeit.default_timer()
	algorithm(text, pattern)
	end_time = timeit.default_timer()
	execution_time = end_time - start_time
	return execution_time


def main():
	article1_path = 'article_1.txt'
	article2_path = 'article_2.txt'

	article1_text = read_file(article1_path)
	article2_text = read_file(article2_path)

	real_substring_art_1 = "Він корисний"
	real_substring_art_2 = "Час доступу"
	fake_substring = "вигаданий підрядок"

	# Вимірювання часу виконання для першої статті
	print("Article 1:")
	print("Real substring:")
	print("Rabin-Karp:", measure_algorithm(rabin_karp_search, article1_text, real_substring_art_1))
	print("Boyer-Moore:", measure_algorithm(boyer_moore_search, article1_text, real_substring_art_1))
	print("KMP:", measure_algorithm(kmp_search, article1_text, real_substring_art_1))
	print("\nFake substring:")
	print("Rabin-Karp:", measure_algorithm(rabin_karp_search, article1_text, fake_substring))
	print("Boyer-Moore:", measure_algorithm(boyer_moore_search, article1_text, fake_substring))
	print("KMP:", measure_algorithm(kmp_search, article1_text, fake_substring))

	# Вимірювання часу виконання для другої статті
	print("\nArticle 2:")
	print("Real substring:")
	print("Rabin-Karp:", measure_algorithm(rabin_karp_search, article2_text, real_substring_art_2))
	print("Boyer-Moore:", measure_algorithm(boyer_moore_search, article2_text, real_substring_art_2))
	print("KMP:", measure_algorithm(kmp_search, article2_text, real_substring_art_2))
	print("\nFake substring:")
	print("Rabin-Karp:", measure_algorithm(rabin_karp_search, article2_text, fake_substring))
	print("Boyer-Moore:", measure_algorithm(boyer_moore_search, article2_text, fake_substring))
	print("KMP:", measure_algorithm(kmp_search, article2_text, fake_substring))


if __name__ == "__main__":
	main()

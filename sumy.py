class SummerTime:
    def lex_rank_analysis(self,parser_configuration, number_of_lines_to_output):
        #Using LexRank
        from sumy.summarizers.lex_rank import LexRankSummarizer
        summerizer = LexRankSummarizer()
        #Summarize the text and output n sentences
        summarization_result = summarizer(parser_configuration.document, number_of_lines_to_output)
        #Debug raw to console
        print("\Begin Raw summary from LexRank\n")
        for sentence in summarization_result:
            print(sentence)
        print("\nEnd Raw Summary from LexRank\n")
        #Return summer result
        return summarization_result

    def lsa_analysis(self, parser_configuration, number_of_lines_to_output):
        from sumy.summarizers.lsa import LsaSummarizer
        summarizer = LsaSummarizer()
        #Summarize text and output n sentences
        summarization_result = summarizer(parser_configuration.document, number_of_lines_to_output)
        print("\nBegin Raw Summary from LSA\n")
        for sentence in summarization_result:
            print(sentence)
        print("\nEnd Raw summary from LSA\n")
        return summarization_result

    def luhn_analysis(self, parser_configuration, number_of_lines_to_output):
        from sumy.summarizers.luhn import LuhnSummarizer
        summarizer = LuhnSummarizer()
        #Summarize the text and output n sentences
        summarization_result = summarizer(parser_configuration.document, number_of_lines_to_output)
        #Debug raw output to console
        print("\nBegin Raw summary from Luhn\n")
        for sentence in summarization_result:
            print(sentence)
        print("\nEnd Raw summary from Luhn\n")

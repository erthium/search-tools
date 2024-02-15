import { SearchService } from "./search";

describe("SearchService", () => {
    it("should be defined", () => {
        expect(SearchService).toBeDefined();
    });
    
    it("should simplify the word", async () => {
        const word = "éèà";
        const simplified = await SearchService.simplyfy(word);
        expect(simplified).toBe("eea");
    });

    it("should simplify the word", async () => {
        const word = "üöäşçİ";
        const simplified = await SearchService.simplyfy(word);
        expect(simplified).toBe("uoasci");
    });

    it("should find the levenstein distance", async () => {
        const word = "kitten";
        const target = "sitting";
        const distance = await SearchService.levDistance(word, target);
        expect(distance).toBe(3);
    });

    it("should check if word is in target", async () => {
        const word = "hey";
        const target = "hey mom";
        const isIn = await SearchService.wordInWord(word, target);
        expect(isIn).toBe(true);
    });

    it("should find the similarity percentage", async () => {
        const word = "a";
        const target = "aa";
        const similarity = await SearchService.similarity(word, target);
        expect(similarity).toBe(0.5);
    });

    it("should find the similarity percentage", async () => {
        const word = "ab";
        const target = "aa";
        const similarity = await SearchService.similarity(word, target);
        expect(similarity).toBe(0.5);
    });

    it("should find the similarity percentage", async () => {
        const word = "aa";
        const target = "aa";
        const similarity = await SearchService.similarity(word, target);
        expect(similarity).toBe(1);
    });

    it("should check if two words are similar", async () => {
        const str1 = "hey";
        const str2 = "hey mom";
        const isSimilar = await SearchService.isSimilar(str1, str2);
        expect(isSimilar).toBe(true);
    });

    it("should check if two words are not similar", async () => {
        const str1 = "hey";
        const str2 = "there";
        const isSimilar = await SearchService.isSimilar(str1, str2);
        expect(isSimilar).toBe(false);
    });
});
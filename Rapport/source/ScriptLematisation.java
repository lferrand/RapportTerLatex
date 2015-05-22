public class Lemmatisation{
    //....
    public List<TreeTaggerWordWrapper> execution(String pathFile) 
    throws IOException, TreeTaggerException {
        TreeTaggerWrapper taggerWrapper = ....
        final List<TreeTaggerWordWrapper> wordWrappers = ....
        try {
            taggerWrapper.setModel(Constants.TREETAGGER_LANGUAGE);
            taggerWrapper.setHandler(new TokenHandler<String>() {
                public void token(String token, String tag, String lemma) {
                    TreeTaggerWordWrapper word = 
                        new TreeTaggerWordWrapper(token, tag, lemma);
                    wordWrappers.add(word);
                }
            });
            taggerWrapper.process(readLinesOfFile(pathFile));
        } finally {
            taggerWrapper.destroy();
        }
        return wordWrappers;
    }
    //.....
}

public class TreeTaggerWordWrapper {
    //.....
    public TreeTaggerWordWrapper(String word, String tag, String lemma) {
        //....
        preprocessing();
    }

    private void preprocessing(){
        String []tags = this.tag.split(":");
        if (tags.length > 1){
            this.tag = tags[0]; this.subTag = tags[1];
        }
        this.word = (this.lemma.equals("<unknown>") ? this.word) : 
            (!lemma.contains("|") ? this.lemma : this.lemma.split("\\|")[1]);
     }  
    //.....
}
